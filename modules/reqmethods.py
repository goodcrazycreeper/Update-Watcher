"""
Universe.py responsible for retrieving universe data such as number of subplaces.
"""
import requests

def check_key_exists(d, key): 
    return key in d # Check if the 'address' key exists in the dictionary

def getMethod(*args,**kwargs): # Returns data as "data" dict
    """
    Returns a dictionary, where "data" is the json from the GET request method and status is the status code of the GET method.
    Returns a dictionary, where and if an exception occurs, returns "data" and None and status code as -1.
    """
    
    try:
        r = requests.get(*args,**kwargs)
    except Exception as e:
        print(f"exception as: {e}")
        return {"data": None, "status": -1} # Return none when error occurs
    return {"data": r.json(), "status": r.status_code}

def getUniverseData(placeId): # Nests returned JSON into a keyword 'data'
    """Method to retrieve a JSON about a roblox Universe"""

    GETUNIVERSEID = getMethod(f'https://apis.roblox.com/universes/v1/places/{placeId}/universe')
    Universe_ID = GETUNIVERSEID["data"]
    status = GETUNIVERSEID['status']

    if status == -1:
        result = "No Internet Connection"
    elif Universe_ID["universeId"] == "null":
        result = "placeId does not exist"
    elif check_key_exists(Universe_ID,"universeId") == True: # Check if the dictionary exists
        result = getMethod(f'https://develop.roblox.com/v2/universes/{Universe_ID["universeId"]}/places')
    return result