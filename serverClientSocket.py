# Author : Omkar Dixit
# Source: https://www.geeksforgeeks.org/socket-programming-python/

import socket

# Create a socket
s = socket.socket()
print("Created Socket!")

# reserve any port 
port = 999

# as we know bind() will bind the server to a specific ip and port
# leaving it blank will make it listen to requets coming from other computers of that network
s.bind(('', port))
print("Socket Binded to", port)

# as we know listen() will put the server to listening mode
s.listen(5)
print("Socket Listening!")

# Accept till we get error
while True:
    # Establish Connection with client
    c, addr = s.accept()
    print("Got Connection from ", addr)

    # Send a reply message
    c.send("Thanks for connecting!")

    c.close()
