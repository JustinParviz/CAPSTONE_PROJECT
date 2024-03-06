import requests
import requests_cache 
import json


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