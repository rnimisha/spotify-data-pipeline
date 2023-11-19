def insert_dim_artist(cursor, row):
    artist_natural_key = row["artist_natural_key"]
    artist_name = row["artist_name"]

    cursor.execute(
        "SELECT artist_id FROM dim_artist WHERE artist_natural_key = %s",
        (artist_natural_key,),
    )
    artist_id = cursor.fetchone()

    # Check if the artist exists
    if artist_id:
        return artist_id[0]
    else:
        cursor.execute(
            "INSERT INTO dim_artist (artist_name, artist_natural_key) VALUES (%s, %s) RETURNING artist_id",
            (
                artist_name,
                artist_natural_key,
            ),
        )
        return cursor.fetchone()[0]
