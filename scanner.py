#!/bin/python3

import sys
import socket
from datetime import datetime


#define target
#TODO: add multithreading for port scans
#TODO: add sanity checks for arguments

if len(sys.argv) == 4:
	target = socket.gethostbyname(sys.argv[1]) #translate hostname to IPv4
else:
	print("Error: Missing arguments")
	print("Syntax: python3 scanner.py <IP address> <port start> <port end>")
	sys.exit(2)

print("-" * 40)
print("Scanning target: " + target)
print("Time started: " + str(datetime.now()))
print("-" * 40)

try:
	for port in range(int(sys.argv[2]), int(sys.argv[3])):
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #AF_INET for IPv4
			socket.setdefaulttimeout(1)
			result = s.connect_ex((target, port))
			
			if result == 0: #result == 0 means port is open. result == 1 means port is closed
				print(f"Port {port} is open")

except KeyboardInterrupt:
	print("\nExiting Program.")
	sys.exit(1)

except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit(1)

except socket.error:
	print("Could not connect to the server.")
	sys.exit(1)


