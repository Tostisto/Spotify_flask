import spotipy
import spotipy.util as util

class SpotifyAuth:
    def __init__(self, client_id, client_secret, redirect_uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
    
    def get_token(self, username, scope):
        token = util.prompt_for_user_token(username, scope, client_id=self.client_id,
                                           client_secret=self.client_secret, redirect_uri=self.redirect_uri)
        return token
    
    def authenticate(self, username, scope):
        token = self.get_token(username, scope)
        if token:
            sp = spotipy.Spotify(auth=token)
            return sp
        else:
            print("Can't get token for", username)
