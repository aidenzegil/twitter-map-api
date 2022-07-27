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
    res = twitter_client.GetHomeTimeline()
    return {"message": res}

@app.get("/tweet")
async def root():
    id = 1548398318471942147
    res = twitter_client.GetStatus(id)
    return res

@app.get("/profile")
async def root():
    id = 1721070150
    res = twitter_client.GetUser(id)
    return res

@app.get("/comments")
async def root():
    id = 1551652670561169409 
    res = twitter_client.GetReplies(id)
    return res