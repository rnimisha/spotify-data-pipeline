from settings import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET


class AppConfig:
    def __init__(self) -> None:
        self.spotify_client_id = SPOTIFY_CLIENT_ID
        self.spotify_client_secret = SPOTIFY_CLIENT_SECRET

    def get_spotify_client_id(self) -> str:
        return self.spotify_client_id

    def get_spotify_client_secret(self) -> str:
        return self.get_spotify_client_secret


app_config = AppConfig()
