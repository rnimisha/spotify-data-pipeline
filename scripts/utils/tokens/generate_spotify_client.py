import spotipy
from spotipy import Spotify

from scripts.utils.tokens.token import get_access_token


def generate_spotify_client() -> Spotify:
    """_summary_
    Generates spotify client with spotipy

    Returns:
        Spotify: Spotify client
    """
    access_token = get_access_token()
    spotify_client = spotipy.Spotify(auth=access_token)

    return spotify_client
