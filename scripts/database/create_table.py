import logging

from airflow.decorators import task
from airflow.exceptions import AirflowException
from scripts.database.connection import connect_to_database
from scripts.database.schema import (
    get_dim_artist_create_query,
    get_dim_date_create_query,
    get_dim_song_create_query,
    get_fact_song_stream_create_query,
)


@task
def create_star_schema_table():
    conn = None
    cursor = None
    try:
        conn = connect_to_database()
        cursor = conn.cursor()

        logging.info("Creating tables...........")
        cursor.execute(get_dim_song_create_query())
        cursor.execute(get_dim_artist_create_query())
        cursor.execute(get_dim_date_create_query())
        cursor.execute(get_fact_song_stream_create_query())

        conn.commit()
        logging.info("Tables created successfully....")

    except Exception as e:
        logging.error(f"Error creating tables {e}")
        raise AirflowException(f"Error creating tables {e}")

    finally:
        if cursor is not None:
            cursor.close()

        if conn is not None:
            conn.close()
