class SpotifyArtist:
    def __init__(self, sp, artist_id):
        self.sp = sp
        self.artist_id = artist_id
        print("Artist ID: " + self.artist_id)

    def get_artist(self):
        artist = self.sp.artist(self.artist_id)
        return artist

    def get_artist_albums(self):
        albums = self.sp.artist_albums(self.artist_id)
        return albums

    def get_artist_top_tracks(self):
        top_tracks = self.sp.artist_top_tracks(self.artist_id)
        return top_tracks

    def get_related_artists(self):
        related_artists = self.sp.artist_related_artists(self.artist_id)
        return related_artists

    def get_artist_info(self):
        artist = self.get_artist()
        artist_albums = self.get_artist_albums()
        artist_top_tracks = self.get_artist_top_tracks()
        related_artists = self.get_related_artists()

        artist_info = {
            "artist": artist,
            "albums": artist_albums,
            "top_tracks": artist_top_tracks,
            "related_artists": related_artists
        }

        return artist_info
