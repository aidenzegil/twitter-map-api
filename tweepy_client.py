import tweepy
from config import api_key, api_secret, pat, pat_secret

twitter_client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=pat,
    access_token_secret=pat_secret,
)
