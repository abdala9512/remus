""""Spotify requests"""

from urllib.parse import urlencode
import requests

from .api_connection import SpotifyAPIConnection


class SpotifyRequest(SpotifyAPIConnection):

    BASE_ENDPOINT =  "https://api.spotify.com/v1/"

    def __init__(self, client_id, secret_id):
        SpotifyAPIConnection.__init__(self, client_id, secret_id)
        self.client_id = client_id
        self.secret_id = secret_id
 

    def search(self, query, type):
        """[summary]

        Args:
            query ([String]): it could be "track", "album"
            type ([type]): [description]
        """
        header = {
            "Authorization": f"Bearer {self.access_token}"
        }

        endpoint = BASE_ENDPOINT + "search"
        data = urlencode({"q": query, "type": type})

        lookup_URL = f"{endpoint}?{data}"

        r = requests.get(lookup_URL, headers=header)





