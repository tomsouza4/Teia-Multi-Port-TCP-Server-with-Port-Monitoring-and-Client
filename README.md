# Project Overview

## Purpose

This project provides a flexible TCP server implementation capable of listening on multiple ports simultaneously, as well as a client for checking port connectivity and server responses. It leverages Python's socket and threading libraries to handle concurrent connections efficiently.
  
## Files
- Teia_Client.py: Client script for checking port status.
- Teia_Server.py: Threaded TCP server script that echoes back received data in uppercase.
- ThreadedServer.py: Generic threaded server script that can be used for various server tasks.
- server.py: Threaded TCP server script that echoes back received data without modification.

## Key Features
- Threaded Execution: Servers use threading to handle multiple client connections efficiently.
- File Configuration: Server scripts can read port numbers from a specified file (idm_ports.txt).
- Error Handling: Scripts include basic error handling for socket operations and file access.

## Usage
Teia_Client.py:
- Modify the idm_ports.txt file with a comma-separated list of ports to check.
- Run the script to check port status and log results to ports.txt.
  
Server Scripts:
- Run the server scripts to start listening on specified ports.
- Use a client tool (e.g., telnet) to connect to the servers and interact.

## Potential Applications
- Network testing and troubleshooting
- Simple echo servers for testing client-server interactions
- Simulated network services for development and testing
- Custom server applications built upon the provided framework
  
## Additional Notes
- Dependencies: Python standard library modules (socket, threading, SocketServer).
- Environment: Tested in a Python environment (version not specified).
- Customization: Scripts can be adapted for different network communication scenarios.
