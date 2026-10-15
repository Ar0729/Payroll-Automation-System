import pandas as pd


def process_previous_lop(df, year, month):

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

    current_start = pd.Timestamp(year, month, 1)

    previous_end = current_start - pd.Timedelta(days=1)

    previous_start = previous_end.replace(day=1)

    for _, row in df.iterrows():

        from_date = row["From Date"]

        to_date = row["To Date"]

        if pd.isna(from_date):
            continue

        if pd.isna(to_date):
            to_date = from_date

        leave_type = str(
            row.get("Leave Type", "")
        ).upper()

        if leave_type not in ["LOP", "LOSS OF PAY"]:
            continue

        # Leave overlaps previous month
        if from_date <= previous_end and to_date >= previous_start:

            results.append({
                "Employee ID": row.get("Employee ID"),
                "Employee Name": row.get("Employee Name"),
                "From Date": from_date,
                "To Date": to_date,
                "Days": row.get("No. of Days"),
                "Remarks": (
                    "Previous month LOP carried forward"
                )
            })

    return pd.DataFrame(results)