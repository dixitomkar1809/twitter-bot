# Author : Omkar Dixit
# Reference: https://www.geeksforgeeks.org/socket-programming-python/

import socket

# Create a socket
s = socket.socket()
print("Created Socket!")

# reserve any port 
port = 999

# as we know bind() will bind the server to a specific ip and port
# leaving it blank will make it listen to requets coming from other computers of that network
# if we pass 127.0.0.1 then it will listen to the calls made in the local computer
s.bind(('127.0.0.1', port))
print("Socket Binded to", port)

# as we know listen() will put the server to listening mode
# here 5 means that 5 connections are kept waiting if the server is busy and any more connect they are refused
s.listen(5)
print("Socket Listening!")

# Accept till we get error
while True:
    # Establish Connection with client
    c, addr = s.accept()
    print("Got Connection from ", addr)

    # Send a reply message
    c.send(b"Thanks for connecting!")

    c.close()

# To just check the server Socket
# run the server socket
# open another terminal
# use the follwing command
# telnet localhost 999 
# here 999 because 999 is the one where server is running
