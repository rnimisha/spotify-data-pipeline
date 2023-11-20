def get_fact_song_stream_create_query():
    query = """
        CREATE TABLE IF NOT EXISTS fact_song_stream (
            song_stream_id SERIAL PRIMARY KEY,
            date_id INTEGER REFERENCES dim_date(date_id),
            song_id INTEGER REFERENCES dim_song(song_id),
            artist_id INTEGER REFERENCES dim_artist(artist_id),
            play_count INTEGER DEFAULT 1,
            total_duration INTEGER
        )
    """
    return query
