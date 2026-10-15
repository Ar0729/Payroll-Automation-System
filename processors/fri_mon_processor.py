import pandas as pd


def process_friday_monday(df):

    results = []

    df = df.copy()

    df["From Date"] = pd.to_datetime(
        df["From Date"],
        errors="coerce"
    )

    df = df.sort_values(
        ["Employee ID", "From Date"]
    )

    for employee_id, employee_df in df.groupby(
        "Employee ID"
    ):

        employee_df = employee_df.reset_index(drop=True)

        for i in range(len(employee_df)):

            friday = employee_df.iloc[i]

            friday_date = friday["From Date"]

            if pd.isna(friday_date):
                continue

            # Friday = 4
            if friday_date.weekday() != 4:
                continue

            for j in range(i + 1, len(employee_df)):

                monday = employee_df.iloc[j]

                monday_date = monday["From Date"]

                if pd.isna(monday_date):
                    continue

                difference = (
                    monday_date - friday_date
                ).days

                if difference == 3:

                    results.append({
                        "Employee ID": employee_id,
                        "Employee Name":
                            friday.get(
                                "Employee Name"
                            ),
                        "Friday Date":
                            friday_date,
                        "Monday Date":
                            monday_date,
                        "Remarks":
                            "Friday-Monday leave pattern detected"
                    })

    return pd.DataFrame(results)