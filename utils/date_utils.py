import pandas as pd


def convert_to_datetime(series):
    return pd.to_datetime(series, errors="coerce")


def format_date(value):
    if pd.isna(value):
        return ""

    return pd.to_datetime(value).strftime("%d-%m-%Y")


def get_month_range(year, month):
    start = pd.Timestamp(year=year, month=month, day=1)
    end = start + pd.offsets.MonthEnd(1)

    return start, end


def get_month_name(year, month):
    return pd.Timestamp(year=year, month=month, day=1).strftime("%B %Y")


def is_weekday(value, weekday):
    if pd.isna(value):
        return False

    return pd.Timestamp(value).weekday() == weekday


def is_cl_valid_date(value):
    """
    Tuesday = 1
    Wednesday = 2
    Thursday = 3
    """

    if pd.isna(value):
        return False

    return pd.Timestamp(value).weekday() in {1, 2, 3}