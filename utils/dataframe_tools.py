import pandas as pd


def find_column(df, possible_names):
    """
    Find a column using multiple possible names.
    """

    normalized = {
        column.lower().strip(): column
        for column in df.columns
    }

    for name in possible_names:
        key = name.lower().strip()

        if key in normalized:
            return normalized[key]

    return None


def ensure_columns(df, required_columns):
    missing = [
        column
        for column in required_columns
        if column not in df.columns
    ]

    if missing:
        raise ValueError(
            f"Missing required columns: {missing}"
        )


def remove_empty_rows(df):
    return df.dropna(how="all").reset_index(drop=True)


def add_serial_number(df):
    df = df.copy()
    df.insert(0, "S. No", range(1, len(df) + 1))

    return df