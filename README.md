# Project Overview

## Purpose

This project consists of multiple Python scripts that implement network communication functionalities, including:

- Port Status Checking: Scripts for checking the availability of specified ports on a host.
- Threaded Servers: Server scripts that handle client connections concurrently using threading.
  
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
  
## Additional Notes
- Dependencies: Python standard library modules (socket, threading, SocketServer).
- Environment: Tested in a Python environment (version not specified).
- Customization: Scripts can be adapted for different network communication scenarios.
