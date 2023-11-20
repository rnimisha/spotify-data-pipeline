import pandas as pd
import psycopg2


def insert_dim_artist(cursor: psycopg2.extensions.cursor, row: pd.Series):
    artist_natural_key = row["artist_natural_key"]
    artist_name = row["artist_name"]

    cursor.execute(
        "SELECT artist_id FROM dim_artist WHERE artist_natural_key = %s",
        (artist_natural_key,),
    )
    artist_data = cursor.fetchone()

    # Check if the artist exists
    if artist_data:
        return artist_data[0]
    else:
        cursor.execute(
            "INSERT INTO dim_artist (artist_name, artist_natural_key) VALUES (%s, %s) RETURNING artist_id",
            (
                artist_name,
                artist_natural_key,
            ),
        )
        return cursor.fetchone()[0]


def insert_dim_song(cursor: psycopg2.extensions.cursor, row: pd.Series):
    song_title = row["song_title"]
    duration_ms = row["song_duration_ms"]
    song_natural_key = row["song_natural_key"]

    cursor.execute(
        "SELECT song_id FROM dim_song WHERE song_natural_key = %s",
        (song_natural_key,),
    )
    song_data = cursor.fetchone()

    if song_data:
        return song_data[0]
    else:
        cursor.execute(
            "INSERT INTO dim_song (song_title, duration_ms, song_natural_key) VALUES (%s, %s, %s) RETURNING song_id",
            (
                song_title,
                duration_ms,
                song_natural_key,
            ),
        )
        return cursor.fetchone()[0]


def insert_dim_date(cursor: psycopg2.extensions.cursor, row: pd.Series):
    year = row["year"]
    month = row["month"]
    hour_of_day = row["hour_of_day"]
    day_of_week = row["day_of_week"].lower()

    cursor.execute(
        "SELECT date_id FROM dim_date WHERE year = %s AND month = %s AND hour_of_day = %s AND day_of_week = %s",
        (
            year,
            month,
            hour_of_day,
            day_of_week,
        ),
    )
    date_data = cursor.fetchone()

    if date_data:
        return date_data[0]
    else:
        cursor.execute(
            "INSERT INTO dim_date (year, month, hour_of_day, day_of_week) VALUES (%s, %s, %s, %s) RETURNING date_id",
            (
                year,
                month,
                hour_of_day,
                day_of_week,
            ),
        )
        return cursor.fetchone()[0]


def insert_fact_song_stream(song_id, artist_id, date_id, cursor, row):
    song_duration_ms = int(row["song_duration_ms"])

    cursor.execute(
        "SELECT song_stream_id, play_count,total_duration  FROM fact_song_stream WHERE date_id = %s AND song_id = %s AND artist_id = %s",
        (
            date_id,
            song_id,
            artist_id,
        ),
    )

    fact_song_stream_data = cursor.fetchone()

    if fact_song_stream_data:
        song_stream_id = fact_song_stream_data[0]
        new_play_count = int(fact_song_stream_data[1]) + 1
        new_total_duration = int(fact_song_stream_data[2]) + song_duration_ms

        cursor.execute(
            "UPDATE fact_song_stream SET play_count = %s , total_duration = %s WHERE song_stream_id = %s",
            (new_play_count, new_total_duration, song_stream_id),
        )
        return song_stream_id

    else:
        cursor.execute(
            "INSERT INTO fact_song_stream (date_id, song_id, artist_id, play_count, total_duration) VALUES (%s, %s, %s, %s, %s) RETURNING date_id",
            (
                date_id,
                song_id,
                artist_id,
                1,
                song_duration_ms,
            ),
        )
        return cursor.fetchone()[0]
