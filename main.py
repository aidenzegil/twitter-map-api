from fastapi import FastAPI
from config import api_key, api_secret, auth_token
from tweepy_client import twitter_client

app = FastAPI()


@app.get("/feed")
async def root():
    res = twitter_client.get_home_timeline()
    return {"message": res}


@app.get("/tweet")
async def root():
    id = 1548398318471942147
    res = twitter_client.get_tweet(id, tweet_fields=["author_id"], user_auth = True)
    return res


@app.get("/profile")
async def root():
    id = 1721070150
    res = twitter_client.get_user(id=id, user_auth=True)
    return res


# @app.get("/comments")
# async def root():
#     id = 1553081717132611585
#     # res = twitter_client.GetReplies(id)
#     return res


@app.get("/retweets")
async def root():
    id = 1553081717132611585
    res = twitter_client.retweet(id, user_auth=True)
    return res


@app.get("/tweetLikes")
async def root():
    id = 1553081717132611585
    res = twitter_client.get_liking_users(id=id, user_auth=True)
    return res


@app.get("/userLikes")
async def root():
    id = 1721070150
    res = twitter_client.get_liked_tweets(id=id, user_auth=True)
    return res


@app.get("/following")
async def root():
    id = 1721070150
    res = twitter_client.get_users_following(id=id, user_auth=True)
    return res
