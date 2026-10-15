import pandas as pd


def process_allowance(df):

    results = []

    required_columns = [
        "Employee ID",
        "Allowance Type",
        "Amount"
    ]

    for column in required_columns:

        if column not in df.columns:
            return pd.DataFrame()

    for _, row in df.iterrows():

        amount = pd.to_numeric(
            row["Amount"],
            errors="coerce"
        )

        remark = "Valid allowance"

        if pd.isna(amount):
            remark = "Invalid allowance amount"

        elif amount < 0:
            remark = "Warning: negative allowance"

        results.append({
            "Employee ID":
                row["Employee ID"],

            "Employee Name":
                row.get("Employee Name"),

            "Allowance Type":
                row["Allowance Type"],

            "Amount":
                amount,

            "Status":
                "Valid"
                if not pd.isna(amount) and amount >= 0
                else "Invalid",

            "Remarks":
                remark
        })

    return pd.DataFrame(results)