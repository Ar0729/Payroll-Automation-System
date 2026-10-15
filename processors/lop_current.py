import pandas as pd


def process_current_lop(df, year, month):

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

    month_start = pd.Timestamp(year, month, 1)
    month_end = month_start + pd.offsets.MonthEnd(1)

    for _, row in df.iterrows():

        if pd.isna(row["From Date"]):
            continue

        from_date = row["From Date"]

        to_date = row["To Date"]

        if pd.isna(to_date):
            to_date = from_date

        # Check whether leave overlaps target month
        if from_date <= month_end and to_date >= month_start:

            leave_type = str(
                row.get("Leave Type", "")
            ).upper()

            if leave_type in ["LOP", "LOSS OF PAY"]:

                results.append({
                    "Employee ID": row.get("Employee ID"),
                    "Employee Name": row.get("Employee Name"),
                    "From Date": from_date,
                    "To Date": to_date,
                    "Days": row.get("No. of Days"),
                    "Remarks": (
                        f"Current month LOP detected: "
                        f"{from_date.strftime('%d-%m-%Y')} "
                        f"to "
                        f"{to_date.strftime('%d-%m-%Y')}"
                    )
                })

    return pd.DataFrame(results)