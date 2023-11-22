import sys

sys.path.append("/opt/scripts")

import pandas as pd
from psycopg2.extensions import connection

from airflow.exceptions import AirflowException
from scripts.database.connection import connect_to_database
from scripts.utils.insert_query import (
    insert_dim_artist,
    insert_dim_date,
    insert_dim_song,
    insert_fact_song_stream,
)


def load_processed_data(filename: str):
    try:
        csv_path = f"/opt/data/processed/{filename}"
        df = pd.read_csv(csv_path)
        return df

    except FileNotFoundError:
        raise AirflowException("Processed data file not found.")


def load_to_star_schema(df: pd.DataFrame, conn: connection):
    try:
        cursor = conn.cursor()

        for _, row in df.iterrows():
            artist_id = insert_dim_artist(cursor, row)
            song_id = insert_dim_song(cursor, row)
            date_id = insert_dim_date(cursor, row)
            insert_fact_song_stream(song_id, artist_id, date_id, cursor, row)

    except Exception as e:
        raise AirflowException("Star schema load error: ", e)


def load():
    try:
        df = load_processed_data("processed_played_tracks.csv")
        conn = connect_to_database()

        load_to_star_schema(df, conn)

        conn.commit()
        conn.close()

    except Exception as e:
        raise AirflowException("Loading error: ", e)
