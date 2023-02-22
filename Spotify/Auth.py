import os 
from spotipy import SpotifyOAuth

class Auth:
    def __init__(self):
        # set up the environment variables
        self.client_id = os.environ.get("CLIENT_ID")
        self.client_secret = os.environ.get("CLIENT_SECRET")
        self.redirect_uri = os.environ.get("REDIRECT_URI")
        self.scope = os.environ.get("SCOPES")

    def get_auth(self):
        # return an instance of SpotifyOAuth
        return SpotifyOAuth(client_id=self.client_id, client_secret=self.client_secret,
                            redirect_uri=self.redirect_uri, scope=self.scope)
    
    def auth_url(self):
        # return the authorization URL
        return self.get_auth().get_authorize_url()
    
    def get_access_token(self, code):
        # return the access token
        return self.get_auth().get_access_token(code)