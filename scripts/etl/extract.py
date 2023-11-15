import pandas as pd

from scripts.utils.generate_spotify_client import generate_spotify_client


def extract_spotify_recently_played():
    spotify_client = generate_spotify_client()

    recently_played = spotify_client.current_user_recently_played(limit=10)

    print(len(recently_played["items"]))

    played_track_data = []

    for item in recently_played["items"]:
        track = item["track"]

        track_data_dict = {
            "song_title": track.get("name", "N/A"),
            "artist_name": track["album"]["artists"][0].get("name", "N/A"),
            "played_at": item.get("played_at", "N/A"),
            "song_duration_ms": track.get("duration_ms", "N/A"),
        }
        played_track_data.append(track_data_dict)

    df_columns = ["song_title", "artist_name", "played_at", "song_duration_ms"]
    played_track_df = pd.DataFrame(played_track_data, columns=df_columns)

    csv_filename = "staging_played_tracks.csv"
    played_track_df.to_csv(csv_filename, index=False)

    print(f"DataFrame saved to {csv_filename}")

    return played_track_df
