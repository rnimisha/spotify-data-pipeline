import logging

import psycopg2

from airflow.exceptions import AirflowException
from config.appconfig import app_config


def connect_to_database():
    logging.info("Connecting to postgres database.....")
    try:
        conn = psycopg2.connect(
            dbname=app_config.get_db_name(),
            user=app_config.get_db_user(),
            password=app_config.get_db_password(),
            host=app_config.get_db_host(),
            port=app_config.get_db_port(),
        )

        logging.info("Connected to database.......")
        return conn

    except Exception as e:
        logging.error(f"Error connecting to database: {e}")
        raise AirflowException((f"Error connecting to database: {e}"))
