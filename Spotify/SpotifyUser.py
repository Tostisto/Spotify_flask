class SpotifyUser:
    @staticmethod
    def get_user_info(sp):
        user = sp.current_user()
        return user
    
    @staticmethod
    def get_user_playlists(sp):
        playlists = sp.current_user_playlists()
        return playlists
