# Author: Omkar Dixit
# Source: https://medium.freecodecamp.org/creating-a-twitter-bot-in-python-with-tweepy-ac524157a607

import tweepy
import tkinter
import json
from creds import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Initialize User Object
user = api.me()

# Check your name location etc.
# To get more details from the user object visit 
# https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object.html

print(user.name, user.screen_name, user.location, user.followers_count, user.created_at)


# Follow every follower 
# basically does the work of #Follow4Follow that many people use to get noticed
# Please use carefully if you are just trying to experiment, keep in mind that this will FOLLOW EVERYONE IN YOUR FOLLOWERS LIST

for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
    print("Followed everyone following: " + user.name)


# Retweeting a tweet that has a keyword
# It will automatically retweet the tweet if it has the keyword we are searching for
# If you want to favorite the tweet simply change the tweet.retweet() to tweet.favorite()

keyword = "Sam Curran"
for tweet in tweepy.Cursor(api.search, keyword).items(1):
    try:
        tweet.retweet()
        print("Retweeted the tweet of ", tweet.user.screen_name)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

