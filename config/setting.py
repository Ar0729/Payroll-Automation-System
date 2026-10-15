from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "output"

ABSENCE_FILE = INPUT_DIR / "payroll_sample_data.xlsx"
# RESIGNATION_FILE = INPUT_DIR / "resignation_data.xlsx"

OUTPUT_FILE = OUTPUT_DIR / "payroll_output.xlsx"

DATE_FORMAT = "%d-%m-%Y"

# Business rules
SICK_LEAVE_THRESHOLD = 5

VALID_CL_WEEKDAYS = {
    1,  # Tuesday
    2,  # Wednesday
    3   # Thursday
}