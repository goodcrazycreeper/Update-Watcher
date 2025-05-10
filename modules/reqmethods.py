"""
Universe.py responsible for retrieving universe data such as number of subplaces.
"""
import requests

def CheckKeyExists(d, key): 
    return key in d # Check if the 'address' key exists in the dictionary

def GetMethod(*args,**kwargs): # Returns dictionary: "data"
    """
    Returns a dictionary, where "data" is the json from the GET request method and status is the status code of the GET method.
    Returns a dictionary, where and if an exception occurs, returns "data" and None and status code as -1.
    """
    
    try:
        r = requests.get(*args,**kwargs)
    except Exception as e:
        print(f"exception as: {e} in {__name__}")
        return {"data": None, "status": -1} # Return none when error occurs
    return {"data": r.json(), "status": r.status_code}

def CheckStatusCode(GetDictionary):
    pass
    

def GetUniverseId(PlaceId) -> int:
    r = GetMethod(f'https://apis.roblox.com/universes/v1/places/{PlaceId}/universe')["data"]

    if CheckKeyExists(r,"universeId") == True:
        return r["universeId"]
    else:
        return 1
def GetUniverseData(PlaceId): # Nests returned JSON into a keyword 'data'
    """Method to retrieve a JSON about a roblox Universe"""

    GETUNIVERSEID = GetMethod(f'https://apis.roblox.com/universes/v1/places/{PlaceId}/universe')
    UniverseIdentification = GETUNIVERSEID["data"]
    status = GETUNIVERSEID['status']

    if status == -1:
        result = "No Internet Connection"
    elif UniverseIdentification["universeId"] == "null":
        result = "PlaceId does not exist"
    elif CheckKeyExists(UniverseIdentification,"universeId") == True: # Check if the dictionary exists
        result = GetMethod(f'https://develop.roblox.com/v2/universes/{UniverseIdentification["universeId"]}/places')
    return result