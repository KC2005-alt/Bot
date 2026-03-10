import tweepy
import tkinter

consumer_key = 'NYN1QE666Uwp5wNJg0G8QIJHB'
consumer_secret = 'IznLnZWDy96duDJLv5N8QYVXO0EMufY8UlQ6A1XqrbwTMYSbAW'
access_token = '1642617475358498816-AOoZDUenxrobwwEqVzfR8TYv5wtN6n'
access_token_secret = 'TKtJBfsqWiA8vwZjaK8Qckiv3Z5LDPmrMoLgWvIuor2NF'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

me = client.get_me()
print(me.data.name)


