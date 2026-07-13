# Multi-stage build for the Go Fiber mock server
# Build stage
FROM golang:1.20-alpine AS builder

# Install git for go modules and build dependencies
RUN apk add --no-cache git build-base

WORKDIR /src
# Copy source
COPY . .

# Ensure modules are downloaded
RUN go mod download

# Build binary (disable cgo for static binary)
ENV CGO_ENABLED=0
RUN go build -o /usr/local/bin/mockduux main.go

# Final stage
FROM alpine:3.18
RUN apk add --no-cache ca-certificates

# Create non-root user
RUN addgroup -S app && adduser -S -G app app
USER app

# Copy binary from builder
COPY --from=builder --chown=app:app /usr/local/bin/mockduux /usr/local/bin/mockduux

# Create fixtures directory
WORKDIR /app
VOLUME ["/app/fixtures"]

EXPOSE 3000

ENTRYPOINT ["/usr/local/bin/mockduux"]