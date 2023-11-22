import logging
import time

import pandas as pd

from config.appconfig import app_config


def authorize_user() -> str:
    """_summary_
    Verifies user to generate authorization code
    Returns:
        str: spotify authorization code
    """
    SPOTIFY_CLIENT_ID = app_config.get_spotify_client_id()

    spotify_redirect_uri = "https://www.google.com"
    scope = "user-read-recently-played"

    auth_url = f"https://accounts.spotify.com/authorize?client_id={SPOTIFY_CLIENT_ID}&response_type=code&redirect_uri={spotify_redirect_uri}&scope={scope}"
    print(f"Please visit this URL to authorize the application: {auth_url}")
    authorization_code = input("Enter the authorization code from the callback URL: ")

    return authorization_code
