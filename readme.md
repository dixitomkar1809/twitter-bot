## Introduction

Trying to create and efficient bot to do some analysis of tweets

creds has my consumer_key, consumer_secret, access_token, access_token_secret

Creating scraper to stream live tweets, since during my previous twitter sentimental analysis project the scraper was created and given to us in the course CS 6350 class.

Since I had changed my laptop and the code was creating some errors so rather than just solving the error I preferred creating a similar streamer.

I am planning on using some plotting libraries of python to plot the tweets on the world map based on the sentiment and the location.

Let's see how far I get ahead with this.

Feel free to ask me questions about the code.

Thanks :D

## Socket Programming
*Reference: https://www.geeksforgeeks.org/socket-programming-python/*

Socket is an endpoint used to send or receive data, socket programming is connecting two nodes on a networks to start a communication between them.

One socket will keep listening to something and the other one will reach out to the first one to establish a connection.

Server forms the listener socket while client reaches out to the server.

They are basically what we call as server and client, backbones behind web browsing.

Python has a library called socket, which can be used for Socket programming.

mySocket.py is a simple client socket that we use to connect to Google's Server.

bind() method that binds the server to spefic ip and port to listen to incoming request on that ip and port.

listen() method puts the server to listening mode.

Similarly accept() and close() initiate and close the connection with the client.

_To check if the serverSocket.py is running well or not, so just run the serverSocket.py and open another terminal and run the command **telnet localhost 999**_

If not then run and check the clientSocket.py

## Lets go back to scraper.py

Now in scraper we are taking the tweets with the address then using the Google Geocoding Api we get the lat lnt, after that we get the sentiment of the tweet using TextBlob library.