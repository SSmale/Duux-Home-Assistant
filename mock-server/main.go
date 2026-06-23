package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"strconv"
	"strings"
	"sync"
	"time"

	"github.com/gofiber/fiber/v2"
)

// Device structures - only fields used by integration / tests are included
type Device struct {
	ID                   int             `json:"id"`
	Type                 string          `json:"type"`
	Name                 string          `json:"name"`
	DisplayName          string          `json:"displayName"`
	Owner                string          `json:"owner"`
	DeviceId             string          `json:"deviceId"` // device MAC / id used by commands endpoint
	SensorTypeId         int             `json:"sensorTypeId"`
	Online               bool            `json:"online"`
	ConnectionUpdateDate string          `json:"connectionUpdateDate"`
	ConnectionType       string          `json:"connectionType"`
	SensorType           json.RawMessage `json:"sensorType"`
	Space                json.RawMessage `json:"space"`
	LatestData           LatestData      `json:"latestData"`
}

type LatestData struct {
	DeviceId   *string         `json:"deviceId"`
	PluginName *string         `json:"pluginName"`
	PluginUid  *string         `json:"pluginUid"`
	Data       json.RawMessage `json:"data"`
	FullData   *json.RawMessage `json:"fullData"` // nullable
	Scores     json.RawMessage `json:"scores"`
	Labels     json.RawMessage `json:"labels"`
	Latest     string          `json:"latest"`
}

var (
	devices      []Device
	devicesMutex sync.Mutex
)

func loadFixtures(path string) error {
	f, err := os.Open(path)
	if err != nil {
		return err
	}
	defer f.Close()
	bytes, err := ioutil.ReadAll(f)
	if err != nil {
		return err
	}
	var payload struct {
		Data   []Device        `json:"data"`
		Issues json.RawMessage `json:"issues"`
	}
	if err := json.Unmarshal(bytes, &payload); err != nil {
		return err
	}
	devicesMutex.Lock()
	devices = payload.Data
	devicesMutex.Unlock()
	return nil
}

func saveFixtures(path string) error {
	// Optional: persist current in-memory devices back to file
	// Not used by default; left here for future use.
	devicesMutex.Lock()
	defer devicesMutex.Unlock()
	out := struct {
		Data   []Device `json:"data"`
		Issues []any    `json:"issues"`
	}{
		Data:   devices,
		Issues: []any{},
	}
	b, err := json.MarshalIndent(out, "", "  ")
	if err != nil {
		return err
	}
	return ioutil.WriteFile(path, b, 0644)
}

func findDeviceByMac(mac string) (*Device, int) {
	devicesMutex.Lock()
	defer devicesMutex.Unlock()
	for i := range devices {
		if devices[i].DeviceId == mac {
			return &devices[i], i
		}
		// also allow numeric id matching: e.g., client may provide an integer string
		if strconv.Itoa(devices[i].ID) == mac {
			return &devices[i], i
		}
		// also match name
		if devices[i].Name == mac || devices[i].DisplayName == mac {
			return &devices[i], i
		}
	}
	return nil, -1
}

func applyCommandToDevice(d *Device, cmd string) {
	// Ensure fullData exists (if nil, create empty map)
	var m map[string]interface{}
	if d.LatestData.FullData == nil {
		m = map[string]interface{}{}
	} else {
		if err := json.Unmarshal(*d.LatestData.FullData, &m); err != nil || m == nil {
			m = map[string]interface{}{}
		}
	}

	// Expected commands: "tune set <key> <value>"
	parts := strings.Fields(cmd)
	if len(parts) >= 4 && parts[0] == "tune" && parts[1] == "set" {
		key := parts[2]
		value := strings.Join(parts[3:], " ")

		// Many commands pass binary values as "01" or "00" or plain int strings.
		// Convert numeric strings to int when appropriate.
		intVal, err := strconv.Atoi(value)
		if err == nil {
			// store as int
			switch key {
			case "power":
				// common representation: "01" => 1, "00" => 0
				m["power"] = intVal
			case "sp":
				m["sp"] = intVal
			case "heating", "heatin":
				// integration reads latestData.fullData.heatin
				m["heatin"] = intVal
			case "mode":
				m["mode"] = intVal
			case "night":
				m["night"] = intVal
			case "sleep":
				m["sleep"] = intVal
			case "fan":
				m["fan"] = intVal
			case "dry":
				m["dry"] = intVal
			case "lock":
				m["lock"] = intVal
			case "laundr":
				m["laundr"] = intVal
			case "timer":
				m["timer"] = intVal
			default:
				m[key] = intVal
			}
		} else {
			// non-integer value: store as string
			m[key] = value
		}
	} else {
		// Unknown command: store raw
		m["last_command"] = cmd
	}

	// marshal back to json and set
	b, _ := json.Marshal(m)
	raw := json.RawMessage(b)
	d.LatestData.FullData = &raw
	// update latest timestamp
	d.LatestData.Latest = time.Now().UTC().Format(time.RFC3339)
}

func main() {
	// fixtures path
	fixtures := "./fixtures/devices.json"
	if err := loadFixtures(fixtures); err != nil {
		log.Printf("Warning: failed to load fixtures from %s: %v", fixtures, err)
		// continue with empty devices
		devices = []Device{}
	}

	app := fiber.New()

	// Login endpoint - accepts any credentials and returns a mock JWT
	app.Post("/auth/v4/login", func(c *fiber.Ctx) error {
		var body map[string]interface{}
		if err := c.BodyParser(&body); err != nil {
			// accept empty body
		}
		email := ""
		if v, ok := body["email"].(string); ok {
			email = v
		}
		resp := map[string]interface{}{
			"jwt": map[string]interface{}{
				"access_token": "mock-access-token",
				"expires_in":   3600,
			},
			"user": map[string]interface{}{
				"email": email,
				"id":    1,
			},
		}
		return c.Status(200).JSON(resp)
	})

	// GET sensors - return the full devices list
	app.Get("/smarthome/sensors", func(c *fiber.Ctx) error {
		devicesMutex.Lock()
		defer devicesMutex.Unlock()

		// Optionally allow query param to force modes for testing:
		// ?force_tcp=1 will set latestData.fullData to null for all devices (simulate TCP-mode)
		forceTCP := c.Query("force_tcp", "0")
		outDevices := make([]Device, len(devices))
		copy(outDevices, devices)
		if forceTCP != "0" {
			for i := range outDevices {
				outDevices[i].LatestData.FullData = nil
				outDevices[i].ConnectionType = "tcp"
			}
		}
		return c.JSON(map[string]interface{}{
			"data":   outDevices,
			"issues": []interface{}{},
		})
	})

	// POST commands
	app.Post("/sensor/:deviceMac/commands", func(c *fiber.Ctx) error {
		mac := c.Params("deviceMac")
		var body struct {
			Command string `json:"command"`
		}
		if err := c.BodyParser(&body); err != nil {
			return c.Status(400).JSON(map[string]interface{}{
				"error": "invalid body",
			})
		}

		device, idx := findDeviceByMac(mac)
		if device == nil {
			return c.Status(404).JSON(map[string]interface{}{
				"error": fmt.Sprintf("device %s not found", mac),
			})
		}

		// Apply the command
		applyCommandToDevice(device, body.Command)

		// write back to slice (because device is a pointer to element in slice, it's already updated)
		devicesMutex.Lock()
		devices[idx] = *device
		devicesMutex.Unlock()

		// Simple success response
		return c.Status(200).JSON(map[string]interface{}{
			"success": true,
			"message": "command applied",
			"device":  device.DeviceId,
		})
	})

	// simple endpoint to fetch a single device by mac (helpful for debugging)
	app.Get("/smarthome/sensors/:deviceMac", func(c *fiber.Ctx) error {
		mac := c.Params("deviceMac")
		device, _ := findDeviceByMac(mac)
		if device == nil {
			return c.Status(404).JSON(map[string]interface{}{"error": "not found"})
		}
		return c.JSON(device)
	})

	port := os.Getenv("PORT")
	if port == "" {
		port = "3000"
	}
	log.Printf("Mock Duux server starting on :%s", port)
	log.Fatal(app.Listen(":" + port))
}