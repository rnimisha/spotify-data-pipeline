import base64

import requests

from config.config import app_config


def get_access_token():
    auth_string = (
        f"{app_config.get_spotify_client_id()}:{app_config.get_spotify_client_secret()}"
    )
    base64_encoded = base64.b64encode(auth_string.encode()).decode()

    spotify_url = "https://accounts.spotify.com/api/token"
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {base64_encoded}",
    }

    data = {
        "grant_type": "client_credentials",
        "code": app_config.get_spotify_code(),
        "redirect_uri": "www.google.com",
    }

    response = requests.post(url=spotify_url, data=data, headers=headers)
    response_json = response.json()

    access_token = response_json.get("access_token")
    refresh_token = response_json.get("refresh_token")

    return access_token, refresh_token
