"""Spotify API connection"""

import requests
import json
import base64

class SpotifyAPIConnection:

    TOKEN_URL = 'https://accounts.spotify.com/api/token'


    def __init__(self, client_id, secret): 
        self.client_id = client_id
        self.secret = secret
        self._access_token = None

    @property
    def access_token():
        return self._access_token

    def get_token(self):
        client_creds = f"{self.client_id}:{self.secret}"
        client_creds64 =  base64.b64encode(client_creds.encode())

        token_data = {
            'grant_type': 'client_credentials'
        }

        token_header = {
            'Authorization': f"Basic {client_creds64.decode()}"
        }

        r = requests.post(TOKEN_URL, data=token_data, headers=token_header)
        if r.status_code not in range(200,299)
            return False
        self._access_token =  r.json()['access_token']
        return True
