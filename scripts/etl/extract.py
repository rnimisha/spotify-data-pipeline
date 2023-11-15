from scripts.utils.generate_spotify_client import generate_spotify_client


def extract_spotify_recently_played():
    spotify_client = generate_spotify_client()

    recently_played = spotify_client.current_user_recently_played(limit=10)

    print(len(recently_played["items"]))

    return recently_played["items"]
