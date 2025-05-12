""" 
This module is responsible for getting the dates of when a subplace in a universe was updated.
"""
import reqmethods as req
from reqmethods import GetUniverseData, GetMethod
from env import loadEnvironmentVar

X_API_KEY = loadEnvironmentVar("KEY")

class Universe(): # A class named universe, which a group of places/games with one of the places being the rootPlace(game page)
    # — Class variables shared with every Universe —
    PlaceId: int = 0 # ID used to fetch universe data
    UniverseId: int = 0 # req.GetUniverseId(PlaceId)
    UniverseName: str = ""
    RootPlaceId: int = 1
    Path: str = f"universes/{PlaceId}/places/{UniverseId}"
    
    def __init__(self, PlaceId): # Class constructor
        self.PlaceId = PlaceId # ID used to fetch universe data
        self.UniverseId = req.GetUniverseId(PlaceId)
        self.UniverseName: str
        self.RootPlaceId: int 
        self.Path

#     def _DefineUniverse(Id):
#         r = GetUniverseData(Id)
#         for i in r["data"]:
#             print(i)
# print(Universe)

class Subplace(Universe): # A classed named subplace, which belongs to a universe which defines a place 
    def __init__(self, PlaceId):
        super().__init__(PlaceId)
        self.IsRootPlace: bool = False # Bool
        self._UpdateTime: str = None
        self._DisplayName: str = None

    
    # def FillInfo(self):
    #     url = f"https://apis.roblox.com/cloud/v2/universes/{UniverseId}/places/{PlaceId}"
    #     r =  GetMethod(url,headers=X_API_KEY)["data"]
    #     self._UpdateTime = r["updateTime"]
    #     self._DisplayName = r["displayName"]