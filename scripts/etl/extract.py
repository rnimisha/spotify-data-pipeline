import datetime
import os

import pandas as pd

from scripts.utils.generate_spotify_client import generate_spotify_client
from scripts.utils.save_df_csv import save_df_as_csv


def extract_single_track_data(track_item):
    """
    Extract relevant data only for single track.
    """
    track = track_item["track"]
    track_data_dict = {
        "song_title": track.get("name", "N/A"),
        "artist_name": track["album"]["artists"][0].get("name", "N/A"),
        "played_at": track_item.get("played_at", "N/A"),
        "song_duration_ms": track.get("duration_ms", "N/A"),
        "artist_natural_key": track["album"]["artists"][0].get("id"),
        "song_natural_key": track.get("id"),
    }
    return track_data_dict


def extract_spotify_recently_played() -> pd.DataFrame:
    """
    Fetch recently played songs from spotify playlist.
    Extract relevat track information.
    """
    try:
        spotify_client = generate_spotify_client()

        today = datetime.datetime.now()
        yesterday = today - datetime.timedelta(days=1)
        yesterday_unix_timestamp_ms = int(yesterday.timestamp()) * 1000

        # extract yestarday data only
        recently_played = spotify_client.current_user_recently_played(
            limit=50, after=yesterday_unix_timestamp_ms
        )

        played_track_data = [
            extract_single_track_data(item) for item in recently_played["items"]
        ]

        df_columns = [
            "song_title",
            "artist_name",
            "played_at",
            "song_duration_ms",
            "artist_natural_key",
            "song_natural_key",
        ]
        played_track_df = pd.DataFrame(played_track_data, columns=df_columns)

        return played_track_df

    except Exception as e:
        print("Error during extraction of data from spoify")
        return pd.DataFrame()


def save_to_staging_csv(df: pd.DataFrame):
    """
    Store extracted data to staging layer as csv file.
    """
    csv_filename = "staging_played_tracks.csv"
    csv_path = os.path.join("data/staging", csv_filename)
    save_df_as_csv(df, csv_path)


def extract():
    try:
        df = extract_spotify_recently_played()
        save_to_staging_csv(df)
    except Exception as e:
        print(e)
