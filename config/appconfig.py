from config.settings import (
    DB_HOST,
    DB_NAME,
    DB_PASSWORD,
    DB_PORT,
    DB_USER,
    MY_SPOTIFY_PASSWORD,
    MY_SPOTIFY_USERNAME,
    SPOTIFY_ACCESS_TOKEN,
    SPOTIFY_AUTHORIZATION_CODE,
    SPOTIFY_CLIENT_ID,
    SPOTIFY_CLIENT_SECRET,
    SPOTIFY_CODE,
    SPOTIFY_REDIRECT_URI,
)


class AppConfig:
    def __init__(self) -> None:
        self.spotify_client_id = SPOTIFY_CLIENT_ID
        self.spotify_client_secret = SPOTIFY_CLIENT_SECRET
        self.spotify_code = SPOTIFY_CODE
        self.db_name = DB_NAME
        self.db_user = DB_USER
        self.db_password = DB_PASSWORD
        self.db_host = DB_HOST
        self.db_port = DB_PORT
        self.spotify_access_token = SPOTIFY_ACCESS_TOKEN
        self.spotify_authorization_code = SPOTIFY_AUTHORIZATION_CODE
        self.spotify_redirect_url = SPOTIFY_REDIRECT_URI
        self.my_spotify_username = MY_SPOTIFY_USERNAME
        self.my_spotify_password = MY_SPOTIFY_PASSWORD

    def get_spotify_client_id(self) -> str:
        return self.spotify_client_id

    def get_spotify_client_secret(self) -> str:
        return self.spotify_client_secret

    def get_spotify_code(self) -> str:
        return self.spotify_code

    def get_db_name(self) -> str:
        return self.db_name

    def get_db_user(self) -> str:
        return self.db_user

    def get_db_password(self) -> str:
        return self.db_password

    def get_db_host(self) -> str:
        return self.db_host

    def get_db_port(self) -> int:
        return self.db_port

    def get_spotify_access_token(self) -> str:
        return self.spotify_access_token

    def get_spotify_authorization_code(self) -> str:
        return self.spotify_authorization_code

    def get_spotify_redirect_uri(self) -> str:
        return self.spotify_redirect_url

    def get_my_spotify_username(self) -> str:
        return self.my_spotify_username

    def get_my_spotify_password(self) -> str:
        return self.my_spotify_password


app_config = AppConfig()
