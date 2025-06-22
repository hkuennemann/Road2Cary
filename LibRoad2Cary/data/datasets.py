"""
datasets.py

Provides functionality for loading team progress data from CSV files based on a given date.

This module defines a utility function `get_data` which reads a `team_progress.csv` file
located in a date-specific folder under the `Data/` directory. It returns the data as a pandas
DataFrame or `None` if the file is not found or an error occurs.

Usage Example:
    df = get_data("06_22_25")

Dependencies:
    - os
    - pandas
"""
import os
import pandas as pd

TEAM_PROGRESS_DF = None

def get_data(date: str):
    """
    Loads team progress data from a CSV file corresponding to the given date.

    Args:
        date (str): The date string in 'MM_DD_YY' format (e.g., '06_22_25') used to locate the data file.

    Returns:
        pd.DataFrame or None: A DataFrame containing team progress data if the file is found and readable;
                              otherwise, returns None with an error message.
    """
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
