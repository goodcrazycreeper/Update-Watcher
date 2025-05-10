import modules.reqmethods as req
from modules.reqmethods import GetMethod
import modules.classes as Classes
from dotenv import load_dotenv
import os
import requests
load_dotenv()
X_API_KEY = {"X-API-KEY":os.getenv("X-API-KEY")}
# r =  req.GetMethod("https://apis.roblox.com/cloud/v2/universes/7296012067/places/83139067970039",headers=X_API_KEY)
# print(r)

# sub = Classes.Subplace(7296012067)

# print(req.GetUniverseId(331811267))

# print(GetMethod("https://apis.roblox.com/universes/v1/places/331811267/universe"))

print(req.GetUniverseData(124180448122765))