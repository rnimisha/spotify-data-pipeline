def get_dim_song_create_query():
    query = """
        CREATE TABLE IF NOT EXISTS dim_song (
            song_id SERIAL PRIMARY KEY,
            song_title VARCHAR(255),
            duration_ms INTEGER
        )
    """
    return query
