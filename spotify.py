import json
import spotipy

def get_spotify(access_token):
    token = access_token.replace("'", "\"")

    data = json.loads(str(token))

    return spotipy.Spotify(auth=data["access_token"])