import pandas as pd


def load_excel(file_path):
    try:
        df = pd.read_excel(file_path)

        if df.empty:
            raise ValueError(f"File is empty: {file_path}")

        print(f"Loaded: {file_path}")
        print(f"Rows: {len(df)}")

        return df

    except FileNotFoundError:
        raise FileNotFoundError(
            f"Input file not found: {file_path}"
        )

    except Exception as e:
        raise RuntimeError(
            f"Unable to read {file_path}: {e}"
        )


def normalize_columns(df):
    df = df.copy()

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    return df