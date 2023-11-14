from spotipy.oauth2 import SpotifyOAuth

from config.config import app_config


def authorize_user() -> SpotifyOAuth:
    SPOTIPY_CLIENT_ID = app_config.get_spotify_client_id()
    SPOTIPY_CLIENT_SECRET = app_config.get_spotify_client_secret()
    SPOTIPY_REDIRECT_URI = "https://www.google.com"

    sp_oauth = SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope="user-read-recently-played",
        cache_path=".spotify_cache",
    )

    sp_token_info = sp_oauth.get_cached_token()

    if not sp_token_info:
        auth_url = sp_oauth.get_authorize_url()
        print(f"Please visit this URL to authorize the application: {auth_url}")

        authorization_code = input(
            "Enter the authorization code from the callback URL: "
        )

        sp_token_info = sp_oauth.get_access_token(authorization_code)

    if sp_oauth.is_token_expired(sp_token_info):
        sp_token_info = sp_oauth.refresh_access_token(sp_token_info["refresh_token"])

    sp_oauth.cache_path = ".spotify_cache"
    sp_oauth._save_token_info(sp_token_info)

    return sp_oauth
