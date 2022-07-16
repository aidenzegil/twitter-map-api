from fastapi import FastAPI
from config import api_key, api_secret, auth_token
from twitter_client import twitter_client

app = FastAPI()



@app.get("/")
async def root():
    res = twitter_client.VerifyCredentials()
    return {"message": res}
    
@app.get("/feed")
async def root():
    return {"message": "feed"}

@app.get("/tweet")
async def root():
    return {"Author": "AuthorID", "LikedBy": [{123, 321, 213, 312}], "Comments" : [{123, 321, 213, 312}]}

@app.get("/profile")
async def root():
    return {"Author": "AuthorID", "LikedBy": [{123, 321, 213, 312}], "Comments" : [{123, 321, 213, 312}]}