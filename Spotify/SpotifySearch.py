class SpotifySearch:
    def __init__(self, spotify):
        self.spotify = spotify

    @staticmethod
    def search_album(spotify, album):
        try:
            return spotify.search(q=album, type='album')
        except Exception as e:
            print(f"Error searching album {album}: {str(e)}")
            return None

    @staticmethod
    def search_artist(spotify, artist):
        try:
            return spotify.search(q=artist, type='artist')
        except Exception as e:
            print(f"Error searching artist {artist}: {str(e)}")
            return None
    
    @staticmethod
    def search_track(spotify, track):
        try:
            return spotify.search(q=track, type='track')
        except Exception as e:
            print(f"Error searching track {track}: {str(e)}")
            return None

    @staticmethod
    def search_playlist(spotify, playlist):  
        try:
            return spotify.search(q=playlist, type='playlist')
        except Exception as e:
            print(f"Error searching playlist {playlist}: {str(e)}")
            return None
