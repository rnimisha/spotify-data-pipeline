import pandas as pd


def check_empty_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Check if data frame is empty.
    If empty then stop the pipeline
    """
    if df.empty:
        print("No songs streamed for yesterday. Stoping the process...")
        exit()
    return df


def check_missing_value(df: pd.DataFrame) -> pd.DataFrame:
    # if whole row is empty null
    df = df.dropna(how="all")

    # replace with unknown placeholder
    string_columns = ["song_title", "artist_name"]
    df[string_columns] = df[string_columns].fillna("N/A")

    # if duration or timestamp is missing then whole row is dropped
    df = df.dropna(subset=["song_duration_ms", "played_at"], how="any")
