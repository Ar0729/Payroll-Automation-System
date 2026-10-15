import os
import pandas as pd

from config.setting import (
    ABSENCE_FILE,
    # RESIGNATION_FILE,
    OUTPUT_FILE,
    OUTPUT_DIR
)

from utils.file_loader import load_excel

from processors.lop_current import (
    process_current_lop
)

from processors.lop_previous import (
    process_previous_lop
)

from processors.repeated_sick import (
    process_repeated_sick
)

from processors.maternity_leave import (
    process_maternity_leave
)

from processors.fri_mon_processor import (
    process_friday_monday
)

from processors.sandwich_leave import (
    process_sandwich_leave
)

from processors.resignees import (
    process_resignees
)

from processors.allowance import (
    process_allowance
)

from utils.excel_writer import (
    write_excel
)


def detect_processing_month(df):

    df = df.copy()

    df["From Date"] = pd.to_datetime(
        df["From Date"],
        errors="coerce"
    )

    valid_dates = df[
        "From Date"
    ].dropna()

    if valid_dates.empty:
        raise ValueError(
            "No valid dates found in input."
        )

    latest_date = valid_dates.max()

    return (
        latest_date.year,
        latest_date.month
    )


def main():

    print("=" * 60)
    print("PAYROLL AUTOMATION SYSTEM")
    print("=" * 60)

    os.makedirs(
        OUTPUT_DIR,
        exist_ok=True
    )

    # --------------------------------
    # Load absence data
    # --------------------------------

    print("\nLoading absence data...")

    absence_df = load_excel(
        ABSENCE_FILE
    )

    # --------------------------------
    # Detect month
    # --------------------------------

    year, month = detect_processing_month(
        absence_df
    )

    print(
        f"\nProcessing month: "
        f"{month:02d}-{year}"
    )

    # --------------------------------
    # Run processors
    # --------------------------------

    results = {}

    print("\nRunning processors...")

    print("1. Current LOP")

    results["Current_month"] = (
        process_current_lop(
            absence_df,
            year,
            month
        )
    )

    print("2. Previous LOP")

    results["Previous_month"] = (
        process_previous_lop(
            absence_df,
            year,
            month
        )
    )

    print("3. Repeated Sick Leave")

    results["Repeated Sick Leave"] = (
        process_repeated_sick(
            absence_df
        )
    )

    print("4. Maternity Leave")

    results["Maternity Leave"] = (
        process_maternity_leave(
            absence_df
        )
    )

    print("5. Friday-Monday")

    results["Mon-Fri"] = (
        process_friday_monday(
            absence_df
        )
    )

    print("6. Sandwich Leave")

    results["Sandwich Leave"] = (
        process_sandwich_leave(
            absence_df
        )
    )

    # --------------------------------
    # Resignation
    # --------------------------------

    # if RESIGNATION_FILE.exists():

    #     print("7. Resignees")

    #     resignation_df = load_excel(
    #         RESIGNATION_FILE
    #     )

    #     results["Resignees"] = (
    #         process_resignees(
    #             resignation_df
    #         )
    #     )

    # --------------------------------
    # Allowance
    # --------------------------------

    if "Allowance Type" in absence_df.columns:

        print("8. Allowance")

        results["Allowance"] = (
            process_allowance(
                absence_df
            )
        )

    # --------------------------------
    # Generate Excel
    # --------------------------------

    print("\nGenerating report...")

    write_excel(
        results,
        OUTPUT_FILE
    )

    print("\n" + "=" * 60)
    print("DONE!")
    print("=" * 60)


if __name__ == "__main__":
    main()