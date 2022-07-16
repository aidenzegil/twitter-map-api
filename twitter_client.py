import twitter
from config import api_key, api_secret, pat, pat_secret

twitter_client = twitter.Api(consumer_key=api_key, 
                        consumer_secret=api_secret,
                      access_token_key=pat,
                      access_token_secret=pat_secret)