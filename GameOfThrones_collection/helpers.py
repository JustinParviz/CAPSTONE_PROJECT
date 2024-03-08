from flask import Flask, request, jsonify
from base64 import b64encode


import requests
import requests_cache 
import json
import decimal


#setup our api cache location (this is going to make a temporary database storage for our api calls)

requests_cache.install_cache('image_cache', backend='sqlite')


def get_character():

    # 4 parts to every api:
    # url Required
    # queries/paremeters Optional
    # headers/authorization Optional
    # body/posting Optional

    url = "https://game-of-thrones1.p.rapidapi.com/Characters"

    headers = {
        "X-RapidAPI-Key": "9e09cb3e92msh7c5f921f5308e17p13ff60jsn6d2ec39a8da0",
        "X-RapidAPI-Host": "game-of-thrones1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    data = response.json()

    return data



class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal): #if the object is a decimal we are going to encode it 
                return str(obj)
        return json.JSONEncoder(JSONEncoder, self).default(obj) #if not the JSONEncoder from json class can handle it
    



# *** SPOTIFY API ***
    
app = Flask(__name__)


# Spotify API credentials
CLIENT_ID = "5cf48f0b3d714f848e8aa1877f8a3aa3"
CLIENT_SECRET = "ea358d91e80743b3a62fd9fc430001d5"


def get_token():
    """
    Function to get Spotify access token
    """

    url = "https://accounts.spotify.com/api/token"
    
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic ' + base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()
    }
    body = {
        'grant_type': 'client_credentials'
    }
    response = requests.post(url, headers=headers, data=body)
    data = response.json()
    return data.get('access_token')