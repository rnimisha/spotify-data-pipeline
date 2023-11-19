def get_dim_date_create_query():
    query = """
        CREATE TABLE IF NOT EXISTS dim_date (
            date_id SERIAL PRIMARY KEY,
            year INTEGER,
            month INTEGER,
            hour_of_day INTEGER,
            day_of_week VARCHAR(20),
            CONSTRAINT unique_date_time UNIQUE (year, month, hour_of_day, day_of_week)
        )
    """
    return query
