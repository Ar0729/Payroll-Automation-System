def create_employee_name_map(df):
    mapping = {}

    if "Employee ID" not in df.columns:
        return mapping

    if "Employee Name" not in df.columns:
        return mapping

    for _, row in df.iterrows():

        employee_id = row["Employee ID"]
        employee_name = row["Employee Name"]

        if employee_id and employee_name:
            mapping[employee_id] = employee_name

    return mapping


def add_employee_names(df, employee_map):

    df = df.copy()

    if "Employee ID" not in df.columns:
        return df

    df["Employee Name"] = (
        df["Employee ID"]
        .map(employee_map)
        .fillna("Unknown")
    )

    return df