import pandas as pd

def clean_dataframe(df):
    # Ensure all standard columns exist
    required_cols = ["plant_id", "date", "shift", "bottles_produced", "defect_count", "downtime_minutes"]
    for col in required_cols:
        if col not in df.columns:
            df[col] = None  # Create missing columns as empty

    # Clean 'date'
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # Clean numeric columns
    numeric_cols = ["bottles_produced", "defect_count", "downtime_minutes"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

    # Standardize shift labels (optional)
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
