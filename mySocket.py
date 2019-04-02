# Author: Omkar Dixit
# Source: https://www.geeksforgeeks.org/socket-programming-python/

import socket
import sys

"""
Connect to Google using Socket Programming
"""
# Socket Instance, AF_INET means ipv4 and SOCK_STREAM means connection oriented TCP Protocol
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket Creation Successful!")
except socket.error as err:
    print("Socket Creation Failed: ", err)

# Default port for our socket
port = 80

try:
    host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:
    print("Error in resolving host")
    sys.exit()

# Connecting to the server
s.connect((host_ip, port))

print("Connected to Google at ", host_ip)
