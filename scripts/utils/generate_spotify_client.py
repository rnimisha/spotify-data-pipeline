import spotipy
from spotipy import Spotify

from scripts.utils.authorize_user import authorize_user


def generate_spotify_client() -> Spotify:
    sp_oauth = authorize_user()
    access_token = sp_oauth.get_access_token(as_dict=False)
    spotify_client = spotipy.Spotify(auth=access_token)

    return spotify_client
