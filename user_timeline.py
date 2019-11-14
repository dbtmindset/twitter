import tweepy
import json

with open('config.json') as json_file:
    data = json.load(json_file)
    auth = tweepy.OAuthHandler(data['consumer_key'], data['consumer_secret'])
    auth.set_access_token(data['access_token'], data['access_token_secret'])

    api = tweepy.API(auth)

    public_tweets = api.user_timeline(screenname="dbtmindset", count=50)
    for tweet in public_tweets:
        print(tweet.text + "\n")