import pandas as pd


VALID_CL_DAYS = {1, 2, 3}


def process_sandwich_leave(df):

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

    df["Leave Type"] = (
        df["Leave Type"]
        .astype(str)
        .str.upper()
    )

    for employee_id, employee_df in df.groupby(
        "Employee ID"
    ):

        employee_df = employee_df.sort_values(
            "From Date"
        )

        records = employee_df.to_dict(
            "records"
        )

        for friday in records:

            friday_start = friday["From Date"]

            if pd.isna(friday_start):
                continue

            if friday_start.weekday() != 4:
                continue

            monday_date = (
                friday_start +
                pd.Timedelta(days=3)
            )

            monday_records = [
                r for r in records
                if r["From Date"] == monday_date
            ]

            for monday in monday_records:

                friday_type = friday["Leave Type"]
                monday_type = monday["Leave Type"]

                valid_combination = (
                    friday_type,
                    monday_type
                ) in {
                    ("SL", "CL"),
                    ("CL", "SL"),
                    ("EL", "CL"),
                    ("CL", "EL")
                }

                if not valid_combination:
                    continue

                # Validate CL day
                cl_record = (
                    friday
                    if friday_type == "CL"
                    else monday
                )

                cl_date = cl_record["From Date"]

                cl_valid = (
                    cl_date.weekday()
                    in VALID_CL_DAYS
                )

                remark = (
                    f"Sandwich Leave Detected: "
                    f"{friday_type} on "
                    f"{friday_start.strftime('%d-%m-%Y')} "
                    f"+ "
                    f"{monday_type} on "
                    f"{monday_date.strftime('%d-%m-%Y')}."
                )

                if not cl_valid:

                    remark += (
                        " Warning: CL applied on "
                        "an invalid day."
                    )

                else:

                    weekend_days = [
                        friday_start +
                        pd.Timedelta(days=1),
                        friday_start +
                        pd.Timedelta(days=2)
                    ]

                    weekend_text = ", ".join(
                        d.strftime("%d-%m-%Y")
                        for d in weekend_days
                    )

                    remark += (
                        f" Weekend days "
                        f"({weekend_text}) "
                        f"must be counted as leave."
                    )

                results.append({
                    "Employee ID": employee_id,
                    "Employee Name":
                        friday.get("Employee Name"),
                    "Friday Date":
                        friday_start,
                    "Monday Date":
                        monday_date,
                    "Friday Leave":
                        friday_type,
                    "Monday Leave":
                        monday_type,
                    "Remarks":
                        remark
                })

    return pd.DataFrame(results)