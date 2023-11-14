from spotipy.oauth2 import SpotifyOAuth

from config.config import app_config

SPOTIPY_CLIENT_ID = app_config.get_spotify_client_id()
SPOTIPY_CLIENT_SECRET = app_config.get_spotify_client_secret()
SPOTIPY_REDIRECT_URI = "https://www.google.com"

# Set up Spotipy with OAuth
sp_oauth = SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope="user-read-recently-played",
)

auth_url = sp_oauth.get_authorize_url()

print(f"Please visit this URL to authorize the application: {auth_url}")
