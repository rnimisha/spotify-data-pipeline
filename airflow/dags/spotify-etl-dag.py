import sys
from datetime import datetime, timedelta

sys.path.append("/opt")

from airflow import DAG
from airflow.operators.python import PythonOperator
from scripts.database.create_table import create_star_schema_table
from scripts.etl.extract import extract
from scripts.etl.load import load
from scripts.etl.transform import transform

default_args = {
    "owner": "nayeon",
    "depends_on_past": False,
    "start_date": datetime(2023, 11, 20),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


with DAG(
    "etl_spotify_data_pipeline",
    default_args=default_args,
    description="Data pipeline for ETL DAG for Spotify data",
    schedule_interval="@daily",
    # schedule_interval=timedelta(minutes=1),
) as dag:
    create_tables = PythonOperator(
        task_id="create_tables",
        python_callable=create_star_schema_table,
    )
    extracts = PythonOperator(
        task_id="extract",
        python_callable=extract,
    )
    transforms = PythonOperator(
        task_id="transform",
        python_callable=transform,
        provide_context=True,
        op_kwargs={"filename": "staging_played_tracks.csv"},
    )
    loads = PythonOperator(
        task_id="load",
        python_callable=load,
    )

create_tables >> extracts >> transforms >> loads
