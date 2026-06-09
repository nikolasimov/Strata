# Strata

Strata is an educational HTTP/1.1 web server written from scratch in Python. The project aims to deepen understanding of TCP networking, the HTTP protocol, and object-oriented design through a layered architecture built without external web frameworks.

The goal is not to compete with production servers like nginx or Apache, but to learn how web servers work internally by implementing their core concepts step by step.

## Important
I am proud to announce right now Strata is no longer just a "learning socket project" - it's currently a real minimal functional web server

Just run
python main.py

Then open:
http://127.0.0.1:8080/

## Current Goals

- [x] TCP socket server
- [x] HTTP request parsing
- [x] HTTP response generation
- [x] Routing
- [ ] Middleware pipeline

## Planned Features

- [x] Static file serving
- [ ] Keep-alive connections
- [ ] Selector-based concurrency
- [ ] Configuration system

## Future Ideas

- [ ] HTTPS support using Python's ssl module
- [ ] Request/response logging
- [ ] Template rendering
- [ ] Plugin system

## Disclaimer

Strata is an educational project and is not intended for production use.