import os

import pandas as pd


def load(filename: str):
    try:
        csv_path = os.path.join("data/processed", filename)
        df = pd.read_csv(csv_path)

    except FileNotFoundError:
        print("File to load data not found")
