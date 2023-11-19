def insert_dim_artist(cursor, row):
    artist_name = row["artist_name"].lower()

    cursor.execute(
        "SELECT artist_id FROM dim_artist WHERE LOWER(artist_name) = %s", (artist_name,)
    )
    artist_id = cursor.fetchone()

    # Check if the artist exists
    if artist_id:
        return artist_id[0]
    else:
        cursor.execute(
            "INSERT INTO dim_artist (artist_name) VALUES (%s) RETURNING artist_id",
            (artist_name,),
        )
        return cursor.fetchone()[0]
