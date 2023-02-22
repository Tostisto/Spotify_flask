import base64

class SpotifyPlaylist:
    @staticmethod
    def get_playlist_tracks(sp, playlist_id):
        playlist_tracks = sp.playlist_tracks(playlist_id)
        return playlist_tracks
    
    @staticmethod
    def remove_track_from_playlist(sp, playlist_id, track_id):
        sp.playlist_remove_all_occurrences_of_items(playlist_id, [track_id])

    @staticmethod
    def remove_playlist(sp, playlist_id):
        sp.user_playlist_unfollow(sp.me()['id'], playlist_id)

    @staticmethod
    def create_new_playlist(sp, playlist_name, playlist_description):
        return sp.user_playlist_create(
            user = sp.me()['id'],
            name = playlist_name,
            public = False,
            description = playlist_description
        )
    
    @staticmethod
    def add_playlist_image(sp, playlist_id, image):
        image_data = image.read()
        image_b64 = base64.b64encode(image_data).decode('utf-8')
        sp.playlist_upload_cover_image(playlist_id, image_b64)
