def get_dim_artist_create_query():
    query = """
        CREATE TABLE IF NOT EXISTS dim_artist (
            artist_id SERIAL PRIMARY KEY,
            artist_name VARCHAR(255) UNIQUE
        );
        CREATE INDEX IF NOT EXISTS index_artist_name ON dim_artist(artist_name);
    """
    return query
