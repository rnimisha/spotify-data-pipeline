def get_dim_song_create_query():
    query = """
        CREATE TABLE IF NOT EXISTS dim_song (
            song_id SERIAL PRIMARY KEY,
            song_title VARCHAR(255),
            duration_ms INTEGER,
            song_natural_key VARCHAR(255) UNIQUE
        );
        CREATE INDEX IF NOT EXISTS index_song_natural_key ON dim_song(song_natural_key);
    """
    return query
