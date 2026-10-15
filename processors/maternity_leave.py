import pandas as pd


def process_maternity_leave(df):

    results = []

    df = df.copy()

    df["From Date"] = pd.to_datetime(
        df["From Date"],
        errors="coerce"
    )

    df["To Date"] = pd.to_datetime(
        df["To Date"],
        errors="coerce"
    )

    maternity = df[
        df["Leave Type"]
        .astype(str)
        .str.upper()
        .isin([
            "ML",
            "MATERNITY",
            "MATERNITY LEAVE"
        ])
    ]

    for _, row in maternity.iterrows():

        start = row["From Date"]
        end = row["To Date"]

        if pd.isna(start):
            continue

        if pd.isna(end):
            end = start

        days = (end - start).days + 1

        results.append({
            "Employee ID": row.get("Employee ID"),
            "Employee Name": row.get("Employee Name"),
            "From Date": start,
            "To Date": end,
            "Days": days,
            "Remarks": (
                f"Maternity leave from "
                f"{start.strftime('%d-%m-%Y')} "
                f"to "
                f"{end.strftime('%d-%m-%Y')}"
            )
        })

    return pd.DataFrame(results)