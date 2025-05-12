# reqmethods.py
"""
Universe.py responsible for retrieving universe data such as number of subplaces.
Contains helper functions and methods for api calls
"""
import requests

def CheckKeyExists(dict, key): 
    """Ensures that a key exists before accessing the given key."""
    return key in dict # Check if the 'address' key exists in the dictionary

def GetMethod(*args,**kwargs): # Returns dictionary: "data"
    """
    Returns a dictionary, where "data" is the json from the GET request method and status is the status code of the GET method.
    Returns a dictionary, where and if an exception occurs, returns "data" and None and status code as -1.
    """
    try: Response = requests.get(*args,**kwargs)
    except Exception as e:
        print(f"exception as: {e} in {__name__}")
        return {"data": None, "status": -1} # Return none when error occurs
    return {"data": Response.json(), "status": Response.status_code}
    
def GetUniverseId(PlaceId) -> int:
    """# GetUniverseId:
    Retrieves UniverseID and returns it as a pure integer.\n
    Returns -1 if the universeId field does not exist.
    """
    # Dependencies: GetMethod, CheckKeyExists.
    Response = GetMethod(f'https://apis.roblox.com/universes/v1/places/{PlaceId}/universe')["data"]
    if CheckKeyExists(Response,"universeId") == True:
        Response = Response["universeId"]
        if  Response != "null":
            return Response
    else:
        return -1 # Return if universeId does not exist
def GetUniverseData(PlaceId):
    """Method to retrieve a JSON about a roblox Universe"""
    Response = GetUniverseId(PlaceId)
    if Response == -1:
        raise Exception("Universe Field does not exist")
    return GetMethod(f'https://develop.roblox.com/v2/universes/{Response}/places')