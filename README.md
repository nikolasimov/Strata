# Strata

Strata is an educational HTTP/1.1 web server written from scratch in Python.  
It is designed to explore how web servers work internally by implementing core components such as TCP networking, HTTP parsing, routing, and static file serving without using external web frameworks.

The goal is not to replicate production-grade servers like Nginx or Apache, but to understand their underlying architecture through a minimal, modular implementation.

## Overview

Strata is currently a working minimal web server capable of:

## Current Features

Core HTTP System

-[x]TCP socket server
-[x]HTTP/1.1 request parsing
-[x]HTTP response generation
-[x]Request routing System

Static File Server

-[x]Static file serving from /public
-[x]HTML, CSS, and JS support
-[x]MIME type detection

## Planned Features
-[ ]Reverse proxy
-[ ]Middleware pipeline
-[ ]Keep-alive connections
-[ ]Configuration system
-[ ]Request/Response logging system
-[ ]HTTPS support via Python ssl


## Running the Server

python main.py

Then open :
http://127.0.0.1:8080/


## Disclaimer

Strata is an educational project and is not intended for production use.

## Design Philosophy

Strata is intentionally built in layers:

1. TCP connection handling
2. HTTP parsing
3. Request routing
4. Static file resolution
5. (Planned) proxy + middleware layers

This structure mirrors simplified concepts used in real-world web servers.