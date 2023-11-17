import os

import pandas as pd

from scripts.utils.save_df_csv import save_df_as_csv


def check_empty_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Check if data frame is empty.
    If empty then stop the pipeline
    """
    if df.empty:
        print("No songs streamed for yesterday. Stoping the process...")
        exit()
    return df


def check_missing_value(df: pd.DataFrame) -> pd.DataFrame:
    # if whole row is empty null
    df = df.dropna(how="all")

    # replace with unknown placeholder
    string_columns = ["song_title", "artist_name"]
    df[string_columns] = df[string_columns].fillna("N/A")

    # if duration or timestamp is missing then whole row is dropped
    df = df.dropna(subset=["song_duration_ms", "played_at"], how="any")

    return df


def transform_date(df: pd.DataFrame) -> pd.DataFrame:
    df["played_at"] = pd.to_datetime(df["played_at"])
    df["year"] = df["played_at"].dt.year
    df["month"] = df["played_at"].dt.month
    df["hour_of_day"] = df["played_at"].dt.hour
    df["day_of_week"] = df["played_at"].dt.day_name()

    return df


def transform_artist(df: pd.DataFrame) -> pd.DataFrame:
    df["artist_name"] = df["artist_name"].str.lower().str.strip()
    return df


def check_duration_format(duration_value):
    try:
        return int(duration_value)
    except ValueError as error:
        print("Not a valid number")


def transform_song(df: pd.DataFrame) -> pd.DataFrame:
    df["song_title"] = df["song_title"].str.lower().str.strip()
    df["song_duration_ms"] = df["song_duration_ms"].apply(check_duration_format)
    return df


def save_df_to_processed_csv(data_frame):
    csv_filename = "processed_played_tracks.csv"
    csv_path = os.path.join("data/processed", csv_filename)
    save_df_as_csv(data_frame, csv_path)


def transform(filename: str) -> pd.DataFrame:
    try:
        # read data from staging layer
        csv_path = os.path.join("data/staging", filename)
        df = pd.read_csv(csv_path)

        # apply transformations
        df = check_empty_data(df)
        df = check_missing_value(df)
        df = transform_date(df)
        df = transform_artist(df)
        df = transform_song(df)

        # save processed data
        save_df_to_processed_csv(df)

        return df

    except FileNotFoundError:
        print("Staging file not found")
        return pd.DataFrame()

    except Exception as e:
        print("Unexpected error encountered while transforming data: ", e)
        return pd.DataFrame()
