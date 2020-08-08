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
 

    def search(self, query, search_type):
        """Search for a keyword in Spotify 

        Args:
            query (String): The query we want to look up
            search_type (String): it could be "track", "album"
        """

        header = self.get_resource_header()

        endpoint = SpotifyRequest.BASE_ENDPOINT + "search"
        data = urlencode({"q": query, "type": search_type.ower()})

        lookup_URL = f"{endpoint}?{data}"

        r = requests.get(lookup_URL, headers=header)

        if r.status_code not in range(200, 299):
            return {}
        return r.json()

        def get_resource(self, lookup_id, resource_type='albums'):
            endpoint = f"{SpotifyRequest.BASE_ENDPOINT}{resource_type}/{_id}"
            header = self.header_resource()
            r = requests.get(endpoint, headers=header)
            if status_code not in range(200, 299):
                return {}
            return r.json()

        def get_album(self, _id):
            return self.get_resource(_id, resource_type='albums')

        def get_artist(self, _id):
            return self.get_resource(_id, resource_type='artists')

        def get_track(self, _id)
            return self.get_resource(_id, resource_type='track')

        





