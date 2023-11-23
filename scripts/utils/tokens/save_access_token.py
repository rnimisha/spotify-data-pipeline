def save_access_token(access_token):
    with open("/opt/.env", "a") as env_file:
        env_file.write(f"SPOTIFY_ACCESS_TOKEN={access_token}\n")
