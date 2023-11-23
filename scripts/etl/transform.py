import logging

import pandas as pd

from airflow.decorators import task
from airflow.exceptions import AirflowException
from scripts.utils.save_df_csv import save_df_as_csv


def check_empty_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Check if data frame is empty.
    If empty then stop the pipeline

    Args:
        df (pd.DataFrame): staging layer dataframe

    Returns:
        pd.DataFrame: same dataframe
    """
    if df.empty:
        raise AirflowException(
            "No songs streamed for yesterday. Stoping the process..."
        )

    return df


def check_missing_value(df: pd.DataFrame) -> pd.DataFrame:
    """
    Check for missing and null value in spotify data.

    Args:
        df (pd.DataFrame): staging layer dataframe

    Returns:
        pd.DataFrame: dataframe without null value
    """
    # if whole row is empty null
    df = df.dropna(how="all")

    # replace with unknown placeholder
    string_columns = ["song_title", "artist_name"]
    df[string_columns] = df[string_columns].fillna("N/A")

    # if duration or timestamp is missing then whole row is dropped
    df = df.dropna(subset=["song_duration_ms", "played_at"], how="any")

    return df


def transform_date(df: pd.DataFrame) -> pd.DataFrame:
    """
    Tranforms date to datetime format

    Args:
        df (pd.DataFrame): staging layer data

    Returns:
        pd.DataFrame: dataframe with hour, year, month, week extracted
    """
    df["played_at"] = pd.to_datetime(df["played_at"])
    df["year"] = df["played_at"].dt.year
    df["month"] = df["played_at"].dt.month
    df["hour_of_day"] = df["played_at"].dt.hour
    df["day_of_week"] = df["played_at"].dt.day_name()

    # remove timestamp column
    df = df.drop("played_at", axis=1)

    return df


def transform_artist(df: pd.DataFrame) -> pd.DataFrame:
    """
    Tranform artist detail in spotify data

    Args:
        df (pd.DataFrame): staging layer dataframe

    Returns:
        pd.DataFrame: dataframe with trailing while space removed
    """
    df["artist_name"] = df["artist_name"].str.lower().str.strip()
    return df


def check_duration_format(duration_value) -> int:
    try:
        return int(duration_value)
    except ValueError as error:
        raise AirflowException("Duration of song is not a valid number")


def transform_song(df: pd.DataFrame) -> pd.DataFrame:
    """
    Tranform song detail in spotify data

    Args:
        df (pd.DataFrame): staging layer dataframe

    Returns:
        pd.DataFrame: dataframe with valid duration only
    """
    df["song_title"] = df["song_title"].str.lower().str.strip()
    df["song_duration_ms"] = df["song_duration_ms"].apply(check_duration_format)
    return df


@task
def save_df_to_processed_csv(data_frame):
    """
    Store extracted data to staging layer as csv file.
    """
    csv_filename = "processed_played_tracks.csv"
    csv_path = f"/opt/data/processed/{csv_filename}"

    logging.info("Saving processed data.........")
    save_df_as_csv(data_frame, csv_path)

    logging.info("Processed data saved successfully.......")


@task
def transform(filename: str) -> pd.DataFrame:
    """
    Reads data from staging layer.
    Cleans and transforms data from the layer.
    Stores data in processed layer.

    Args:
        filename (str): file name of staging layer csv

    Returns:
        pd.DataFrame: processed dataframe
    """
    try:
        # read data from staging layer
        csv_path = f"/opt/data/staging/{filename}"
        df = pd.read_csv(csv_path)

        logging.info("Transforming staging data.......")
        # apply transformations
        df = check_empty_data(df)
        df = check_missing_value(df)
        df = transform_date(df)
        df = transform_artist(df)
        df = transform_song(df)

        logging.info("Data transformed successfully....")

        return df

    except FileNotFoundError:
        logging.error("Staging file not found to transform")
        raise AirflowException("Staging file not found to transform")

    except Exception as e:
        logging.error("Unexpected error encountered while transforming data: ", e)
        raise AirflowException(
            "Unexpected error encountered while transforming data: ", e
        )
