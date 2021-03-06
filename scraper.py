# Author: Omkar Dixit
# Reference: http://docs.tweepy.org/en/v3.4.0/streaming_how_to.html

import tweepy
import json
import requests
import re
import socket
from textblob import TextBlob
from creds import *

class MyStreamListener(tweepy.StreamListener):

    # Here we just need the places where the location of the tweet is provided to make sure that we can do whatever analysis we want to do, based on the location.
    def on_status(self, status):
        if status.user.location is not None:
            cleanTweet = self.clean_tweet(status.text)
            print(cleanTweet)
            googleMapsURL = "https://maps.googleapis.com/maps/api/geocode/json?address="+status.user.location+"&key="+googleMapsApi
            results = requests.get(url=googleMapsURL)
            data = results.json()
            if len(data['results'])==0:
                return
            if len(data['results'][0]['address_components']) > 0:
                for i in data['results'][0]['address_components']:
                    lat = data['results'][0]['geometry']['location']['lat']
                    lng = data['results'][0]['geometry']['location']['lng']
                    dictItem = {'text': cleanTweet, 'location': status.user.location, 'coordinates': [lat, lng], 'sentiment':self.get_sentiment(cleanTweet)}
                    output = json.dumps(dictItem)
                    print(output)
                    output+="\n"
                    # conn.send(output.encode('utf-8'))
    
    def on_error(self, status_code):
        if status_code==420:
            return False
        else:
            print(status_code)

    # Removes all the emojis and other punctuation to make the tweet clean and ready for sentiment analysis
    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def get_sentiment(self, tweet):
        analysis = TextBlob(tweet)
        if analysis.sentiment.polarity > 0:
            return 'Positive'
        elif analysis.sentiment.polarity==0:
            return 'Neutral'
        else:
            return 'Negative'

if __name__=="__main__":
    # Authorization
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    # Creating Sockets
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.bind(('localhost', 9001))
    # s.listen(1)
    # conn, addr = s.accept()

    # Creating Listener
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = api.auth, listener = myStreamListener)
    myStream.filter(track=['#Trump'])