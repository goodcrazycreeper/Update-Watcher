import modules.reqmethods as reqmethods
from dotenv import load_dotenv
import os
import requests
load_dotenv()
X_API_KEY = {"X-API-KEY":os.getenv("X-API-KEY")}
r =  reqmethods.getMethod("https://apis.roblox.com/cloud/v2/universes/7296012067/places/83139067970039",headers=X_API_KEY)
print(r)