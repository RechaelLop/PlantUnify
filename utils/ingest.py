import pandas as pd
import os

def load_plant_data(filepath):
    try:
        df = pd.read_excel(filepath, engine='openpyxl')
        return df
    except Exception as e:
        print(f"Error reading file {filepath}: {e}")
        return None

def get_column_headers(df):
    return list(df.columns)
