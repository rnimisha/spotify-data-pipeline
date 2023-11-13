from .settings import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_CODE


class AppConfig:
    def __init__(self) -> None:
        self.spotify_client_id = SPOTIFY_CLIENT_ID
        self.spotify_client_secret = SPOTIFY_CLIENT_SECRET
        self.spotify_code = SPOTIFY_CODE

    def get_spotify_client_id(self) -> str:
        return self.spotify_client_id

    def get_spotify_client_secret(self) -> str:
        return self.spotify_client_secret

    def get_spotify_code(self) -> str:
        return self.spotify_code


app_config = AppConfig()
