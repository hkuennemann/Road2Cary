import os
import pandas as pd

TEAM_PROGRESS_DF = None

def get_data(date: str):
    try:
        file_path = os.path.join(
            r"Data",
            date,
            "team_progress.csv"
        )
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"File not found: {file_path}.")
        print("Check if the date input has the format: 'MM_DD_YY', e.g., '06_12_25'.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
