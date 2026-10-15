import pandas as pd


def process_resignees(df):

    results = []

    df = df.copy()

    df["Date of Resignation"] = pd.to_datetime(
        df["Date of Resignation"],
        errors="coerce"
    )

    df["Last Working Day"] = pd.to_datetime(
        df["Last Working Day"],
        errors="coerce"
    )

    for _, row in df.iterrows():

        resignation_date = row[
            "Date of Resignation"
        ]

        lwd = row["Last Working Day"]

        if pd.isna(resignation_date):
            continue

        results.append({
            "Employee ID":
                row.get("Emp ID"),

            "Employee Name":
                row.get("Employee Name"),

            "Date of Resignation":
                resignation_date,

            "Last Working Day":
                lwd,

            "Notice Period Days":
                row.get("Notice Period Days"),

            "Relieving Date":
                row.get("Relieving Date"),

            "Process/Hold":
                row.get("Process/Hold"),

            "Reason":
                row.get("Reason for Resignation"),

            "Asset Clearance":
                row.get("Asset Clearance Completed"),

            "HR Clearance":
                row.get("HR Clearance Completed"),

            "Finance Clearance":
                row.get("Finance Clearance Completed"),

            "Remark":
                row.get("Remark")
        })

    return pd.DataFrame(results)