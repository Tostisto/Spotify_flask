class SpotifyControl:
    @staticmethod
    def play(sp, device_id=None):
        sp.start_playback(device_id=device_id)

    @staticmethod
    def pause(sp, device_id=None):
        sp.pause_playback(device_id=device_id)

    @staticmethod
    def next_track(sp, device_id=None):
        sp.next_track(device_id=device_id)

    @staticmethod
    def previous_track(sp, device_id=None):
        sp.previous_track(device_id=device_id)

    @staticmethod
    def play_track(sp, track_id):
        sp.start_playback(uris=["spotify:track:{}".format(track_id)])

    @staticmethod
    def play_album(sp, album_id):
        sp.start_playback(context_uri="spotify:album:{}".format(album_id))

    @staticmethod
    def play_playlist(sp, playlist_id):
        sp.start_playback(
            context_uri="spotify:playlist:{}".format(playlist_id))
