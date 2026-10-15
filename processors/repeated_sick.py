import pandas as pd


def process_repeated_sick(df):

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

    sick = df[
        df["Leave Type"]
        .astype(str)
        .str.upper()
        .isin(["SL", "SICK LEAVE"])
    ]

    for _, row in sick.iterrows():

        start = row["From Date"]
        end = row["To Date"]

        if pd.isna(start):
            continue

        if pd.isna(end):
            end = start

        days = (end - start).days + 1

        if days > 5:

            results.append({
                "Employee ID": row.get("Employee ID"),
                "Employee Name": row.get("Employee Name"),
                "From Date": start,
                "To Date": end,
                "Days": days,
                "Remarks": (
                    f"Repeated sick leave detected: "
                    f"{days} consecutive days. "
                    f"Requires HR review."
                )
            })

    return pd.DataFrame(results)