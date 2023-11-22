import psycopg2

from config.appconfig import app_config


def connect_to_database():
    try:
        conn = psycopg2.connect(
            dbname=app_config.get_db_name(),
            user=app_config.get_db_user(),
            password=app_config.get_db_password(),
            host=app_config.get_db_host(),
            port=app_config.get_db_port(),
        )

        print("Connected to database")
        return conn

    except Exception as e:
        print("Error connecting to database: ", e)
        return None
