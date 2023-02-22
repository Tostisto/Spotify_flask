import json
from dotenv import load_dotenv
from flask import Flask, request, redirect
from flask_cors import CORS
from spotify import get_spotify
from Spotify.SpotifyArtist import SpotifyArtist
from Spotify.SpotifySearch import SpotifySearch
from Spotify.SpotifyPlaylist import SpotifyPlaylist
from Spotify.SpotifyTrack import SpotifyTrack
from Spotify.SpotifyUser import SpotifyUser
from Spotify.SpotifyControl import SpotifyControl
from Spotify.SpotifyDevices import SpotifyDevices

from Spotify.Auth import Auth

load_dotenv()

app = Flask(__name__)
CORS(app)
auth = Auth()

"""Authentication Routes"""


@app.route("/authenticate", methods=["GET"])
def authenticate():
    # Redirects to the Spotify authentication page.
    return redirect(auth.auth_url())


@app.route('/callback')
def callback():
    # Handles the callback from Spotify authentication.
    code = request.args.get('code')
    if code:
        access_token = auth.get_access_token(code)
        return redirect(f'http://localhost:3000?access_token={access_token}')


"""User routes"""


@app.route("/user", methods=["GET"])
def user_info():
    try:
        access_token = request.args.get("access_token")
        sp = get_spotify(access_token)
        return json.dumps({"status": "ok", "user": SpotifyUser.get_user_info(sp)})
    except:
        return json.dumps({"status": "error"})


@app.route('/user_playlists')
def user_playlists():
    try:
        sp = get_spotify(request.args.get("access_token"))
        return SpotifyUser.get_user_playlists(sp)
    except:
        return json.dumps({"status": "error"})

"""Control routes"""
@app.route('/play')
def play():
    try:
        id = request.args.get('id')
        type = request.args.get('type')

        sp = get_spotify(request.args.get("access_token"))

        if type == "track":
            SpotifyControl.play_track(sp, id)
        elif type == "album":
            SpotifyControl.play_album(sp, id)
        elif type == "playlist":
            SpotifyControl.play_playlist(sp, id)

        return json.dumps({"status": "ok"})
    except Exception as e:
        print(e)
        return json.dumps({"status": "error"})

@app.route('/pause')
def pause():
    try:
        sp = get_spotify(request.args.get("access_token"))
        SpotifyControl.pause(sp)
        return json.dumps({"status": "ok"})
    except:
        return json.dumps({"status": "error"})

@app.route('/play_paused')
def play_paused():
    try:
        sp = get_spotify(request.args.get("access_token"))
        SpotifyControl.play(sp)
        return json.dumps({"status": "ok"})
    except:
        return json.dumps({"status": "error"})

@app.route('/next')
def next():
    try:
        token = request.args.get("access_token")
        sp = get_spotify(token)
        SpotifyControl.next_track(sp)
        return json.dumps({"status": "ok"})
    except:
        return json.dumps({"status": "error"})

@app.route('/previous')
def previous():
    try:
        sp = get_spotify(request.args.get("access_token"))
        SpotifyControl.previous_track(sp)
        return json.dumps({"status": "ok"})
    except: 
        return json.dumps({"status": "error"})  



@app.route('/get_tranding', methods=["GET"])
def get_tranding():
    try:
        access_token = request.args.get("access_token")
        sp = get_spotify(access_token)
        return SpotifyTrack.get_trending(sp)
    except:
        return json.dumps({"status": "error"})



@app.route('/search', methods=["GET"])
def search():
    try:
        query = request.args.get("query")
        type = request.args.get("type")

        sp = get_spotify(request.args.get("access_token"))

        if type == "track":
            return SpotifySearch.search_track(sp, query)
        elif type == "artist":
            return SpotifySearch.search_artist(sp, query)
        elif type == "album":
            return SpotifySearch.search_album(sp, query)
        elif type == "playlist":
            return SpotifySearch.search_playlist(sp, query)
    except:
        return json.dumps({"status": "error"})


"""Artist info routes"""
@app.route('/artist')
def artist():
    try:
        artist_id = request.args.get('id')
        sp = get_spotify(request.args.get("access_token"))

        artist = SpotifyArtist(sp, artist_id)
        return artist.get_artist_info()
    except:
        return json.dumps({"status": "error"})



"""Playlist management routes"""
@app.route("/playlist_tracks")
def playlist_tracks():
    try:
        playlist_id = request.args.get('id')
        sp = get_spotify(request.args.get("access_token"))

        return SpotifyPlaylist.get_playlist_tracks(sp, playlist_id)
    except:
        return json.dumps({"status": "error"})

@app.route("/remove_playlist_track")
def remove_playlist_track():
    try:
        playlist_id = request.args.get('playlist_id')
        track_id = request.args.get('track_id')
        sp = get_spotify(request.args.get("access_token"))

        SpotifyPlaylist.remove_track_from_playlist(sp, playlist_id, track_id)

        return json.dumps({"status": "ok"})
    except:
        return json.dumps({"status": "error"})


@app.route("/remove_playlist")
def remove_playlist():
    try:
        playlist_id = request.args.get('id')
        sp = get_spotify(request.args.get("access_token"))

        SpotifyPlaylist.remove_playlist(sp, playlist_id)

        return json.dumps({"status": "ok"})
    except:
        return json.dumps({"status": "error"})


@app.route('/create_playlist', methods=['POST'])
def create_playlist():
    try:
        image = request.files['image']
        name = request.form['name']
        description = request.form['description']
        access_token = request.form['access_token']

        sp = get_spotify(access_token)

        new_playlist = SpotifyPlaylist.create_new_playlist(sp, name, description)

        # TODO: Fix setting playlist image
        # SpotifyPlaylist.add_playlist_image(sp, new_playlist["id"], image)

        return json.dumps({"status": "ok"})
    except:
        return json.dumps({"status": "error"})


if __name__ == '__main__':
    app.run(port=8000)
