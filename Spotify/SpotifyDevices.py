class SpotifyDevices:
    def __init__(self, spotify):
        self._spotify = spotify

    def get_active_device(self):
        return self._spotify.devices()[0]

    def get_available_devices(self):
        return self._spotify.devices()

    def set_device(self, device_id):
        self._spotify.transfer_playback(device_id)

    def get_device_name(self, device_id):
        for device in self._spotify.devices():
            if device['id'] == device_id:
                return device['name']