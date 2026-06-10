# Strata

Strata is an educational HTTP/1.1 web server written from scratch in Python.
It is designed to explore how web servers work internally by implementing core components such as TCP networking, HTTP parsing, routing, and static file serving — without using external web frameworks.

The goal is not to replicate production-grade servers like Nginx or Apache, but to understand their underlying architecture through a minimal, modular implementation.

## Overview

Strata is currently a working minimal web server capable of handling static file requests over HTTP/1.1.

## Current Features

**Core HTTP System**

- [x] TCP socket server
- [x] HTTP/1.1 request parsing
- [x] HTTP response generation
- [x] Request routing system

**Static File Server**

- [x] Static file serving from `/public`
- [x] HTML, CSS, and JS support
- [x] MIME type detection

## Planned Features

- [x] Reverse proxy
- [x] Middleware pipeline
- [ ] Keep-alive connections
- [x] Configuration system
- [ ] Request/response logging system
- [ ] HTTPS support via Python `ssl`

## Running the Server

```bash
python main.py
```

Includes a demo static vibecoded website open: http://127.0.0.1:8080/

## Design Philosophy

Strata is intentionally built in layers:

1. TCP connection handling
2. HTTP parsing
3. Request routing
4. Static file resolution
5. *(Planned)* Proxy and middleware layers

This structure mirrors simplified concepts used in real-world web servers.

## Disclaimer

Strata is an educational project and is not intended for production use.
