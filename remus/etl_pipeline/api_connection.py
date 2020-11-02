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
    def access_token(self):
        return self._access_token

    def auth(self):
        client_creds = f"{self.client_id}:{self.secret}"
        client_creds64 =  base64.b64encode(client_creds.encode())

        token_data = {
            'grant_type': 'client_credentials'
        }

        token_header = {
            'Authorization': f"Basic {client_creds64.decode()}"
        }

        r = requests.post(SpotifyAPIConnection.TOKEN_URL, data=token_data, headers=token_header)
        if r.status_code not in range(200,299):
            return False
        self._access_token =  r.json()['access_token']
        return True
    
    def get_access_token(self):
        auth_done = self.auth()
        if not auth_done:
            raise Exception("Authentication failed")
        token = self._access_token
        return token

    def get_resource_header(self):
        access_token = self.get_access_token()
        headers = {
            "Authorization": f"Bearer {self.get_access_token()}"
        }
        return headers