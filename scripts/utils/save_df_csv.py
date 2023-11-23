import logging
import os

import pandas as pd

from airflow.exceptions import AirflowException


def save_df_as_csv(data_frame: pd.DataFrame, csv_path: str):
    """
    Store data in dataframe as csv file.
    """
    try:
        if os.path.exists(csv_path):
            os.remove(csv_path)

        data_frame.to_csv(csv_path, index=False)

    except Exception as e:
        logging.error(f"Error saving data to path {csv_path}")
        raise AirflowException(f"Error saving data to path {csv_path}")
