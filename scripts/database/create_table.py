from .connection import connect_to_database
from .schema import (
    get_dim_artist_create_query,
    get_dim_date_create_query,
    get_dim_song_create_query,
    get_fact_song_stream_create_query,
)


def create_star_schema_table():
    conn = connect_to_database()
    cursor = conn.cursor()

    cursor.execute(get_dim_song_create_query())
    cursor.execute(get_dim_artist_create_query())
    cursor.execute(get_dim_date_create_query())
    cursor.execute(get_fact_song_stream_create_query())

    conn.commit()

    cursor.close()
    conn.close()
