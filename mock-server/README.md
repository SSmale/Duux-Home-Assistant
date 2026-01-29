# Duux Mock Server (Go + Fiber)

This mock server implements a small subset of the Duux cloud API used by the Home Assistant integration:

- POST /auth/v4/login
- GET  /smarthome/sensors
- POST /sensor/{deviceMac}/commands

It reads fixtures from `fixtures/devices.json` on startup and serves them. Commands are applied in-memory to the device `latestData.fullData`.

Usage:

1. Prerequisites
   - Go 1.18+ or Docker

2. Prepare
   - Place the provided `fixtures/devices.json` file in `./fixtures/devices.json`

3. Run locally
   - Initialize modules:
     ```
     go mod init mockduux
     go get github.com/gofiber/fiber/v2
     go mod tidy
     go run main.go
     ```
   - The server listens on :3000 by default. Use PORT env var to change.

4. Run with Docker
   - docker build -t mockduux:latest .
   - docker run -p 3000:3000 -v $(pwd)/fixtures:/app/fixtures mockduux:latest

5. Test
   - Login:
     ```
     curl -X POST http://localhost:3000/auth/v4/login -d '{"email":"test","password":"x"}' -H "Content-Type: application/json"
     ```
   - List devices:
     ```
     curl http://localhost:3000/smarthome/sensors
     ```
   - Force TCP mode (returns fullData=null for all devices):
     ```
     curl http://localhost:3000/smarthome/sensors?force_tcp=1
     ```
   - Send a command:
     ```
     curl -X POST http://localhost:3000/sensor/AA:BB:CC:44:55:66/commands \
       -H "Content-Type: application/json" \
       -d '{"command":"tune set sp 24"}'
     ```
     Then GET the sensors again to see the updated `latestData.fullData.sp` value.

Notes:
- Updates are in-memory only. If you want persistence, enable `saveFixtures()` (the function is included).
- Command parsing covers the common patterns used by the integration.
- Fixtures include representative devices for sensorTypeIds used by the integration: 31, 49, 50, 51, 62, 56, 52.

If you want, I can:
- produce a git patch file you can apply,
- add an admin endpoint to reload fixtures at runtime,
- configure the container to persist updates back to fixtures.json automatically,
- or open the PR for you if you grant a push/collaborator permission or provide an access token with push rights.