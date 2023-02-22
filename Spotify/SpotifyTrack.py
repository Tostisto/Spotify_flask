class SpotifyTrack:
    def __init__(self, sp):
        self.sp = sp
        
    @staticmethod
    def get_track(sp, track_id):
        try:
            track = sp.track(track_id)
            return track
        except:
            print("Error retrieving track with ID {}".format(track_id))
            return None

    @staticmethod
    def get_current_track(sp):
        try:
            current_track = sp.current_user_playing_track()
            return current_track
        except:
            print("Error retrieving current track")
            return None
    
    @staticmethod
    def get_audio_features(sp, track_id):
        try:
            audio_features = sp.audio_features(track_id)
            return audio_features
        except:
            print("Error retrieving audio features for track with ID {}".format(track_id))
            return None
    
    @staticmethod
    def get_related_tracks(sp, track_id):
        try:
            related_tracks = sp.recommendations(seed_tracks=[track_id])
            return related_tracks
        except:
            print("Error retrieving related tracks for track with ID {}".format(track_id))
            return None

    @staticmethod
    def get_trending(sp):
        try:
            trending = sp.new_releases()
            return trending
        except:
            print("Error retrieving trending tracks")
            return None
