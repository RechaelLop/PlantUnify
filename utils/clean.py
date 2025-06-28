import pandas as pd

def clean_dataframe(df, plant_name=None):
    required_cols = ["plant_id", "date", "shift", "bottles_produced", "defect_count", "downtime_minutes"]
    for col in required_cols:
        if col not in df.columns:
            df[col] = None

    # Parse date column
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # Convert numeric columns
    numeric_cols = ["bottles_produced", "defect_count", "downtime_minutes"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

    # Handle Plant 5's downtime in hours
    if plant_name == "plant_5":
        df['downtime_minutes'] = df['downtime_minutes'] * 60

    # Standardize shift labels
    if 'shift' in df.columns:
        df['shift'] = df['shift'].astype(str).str.strip().str.upper()
        df['shift'] = df['shift'].replace({
            'A': 'Shift A',
            'B': 'Shift B',
            'C': 'Shift C',
            '1': 'Shift 1',
            '2': 'Shift 2',
            '3': 'Shift 3'
        })

    return df
