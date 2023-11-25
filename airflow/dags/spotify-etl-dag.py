import sys
from datetime import datetime, timedelta

sys.path.append("/opt")

from airflow.decorators import dag
from scripts.database.create_table import create_star_schema_table
from scripts.etl.extract import extract_spotify_recently_played, save_to_staging_csv
from scripts.etl.load import load
from scripts.etl.transform import save_df_to_processed_csv, transform
from scripts.utils.tokens.authorize_user import authorize_user

default_args = {
    "owner": "nayeon",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


@dag(
    schedule_interval="0 0 * * *",
    start_date=datetime(2023, 11, 20),
    catchup=False,
    tags=["spotify_etl"],
    description="Data pipeline for ETL DAG for Spotify data",
    default_args=default_args,
)
def etl_spotify_data_pipeline():
    create_table_task = create_star_schema_table()

    authorize_user_task = authorize_user()

    extract_task = extract_spotify_recently_played()
    save_to_staging_task = save_to_staging_csv(extract_task)
    transform_task = transform("staging_played_tracks.csv")
    save_to_processed_task = save_df_to_processed_csv(transform_task)
    load_task = load()

    (
        [authorize_user_task, create_table_task]
        >> extract_task
        >> save_to_staging_task
        >> transform_task
        >> save_to_processed_task
        >> load_task
    )


etl_spotify_data_pipeline_dag = etl_spotify_data_pipeline()
