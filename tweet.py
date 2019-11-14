import tweepy
import random
import json

def list_random(ran):
    random.shuffle(ran)
    return ran[0]

with open('config.json') as json_file:
    data = json.load(json_file)
    auth = tweepy.OAuthHandler(data['consumer_key'], data['consumer_secret'])
    auth.set_access_token(data['access_token'], data['access_token_secret'])

    api = tweepy.API(auth)

    with open('tweets.txt') as f:
        lines = f.readlines()
        message = list_random(lines)
        api.update_status(message)