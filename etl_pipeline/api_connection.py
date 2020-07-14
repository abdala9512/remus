"""Spotify API connection"""

import requests
import json
import base64


SPOTIFY_ROOT_URL = "https://api.spotify.com"
class ApiConnection:
    
    def __init__(self, api='spotify'):
        self.api = api

    def spotify_connection(self, user):
        pass
    