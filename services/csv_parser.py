import pandas as pd
from dateutil.parser import parse


EXPECTED_COLUMNS = {
    "revenue",
    "visitors",
    "orders",
    "profit"
}


def detect_timestamp_column(df):

    for column in df.columns:

        try:

            parse(str(df[column].iloc[0]))

            return column

        except:

            continue

    return None


def normalize_columns(df):

    df.columns = [

        c.strip().lower()

        for c in df.columns

    ]

    return df


def validate_csv(filepath):

    try:

        df = pd.read_csv(filepath)

    except Exception:

        return False, "Invalid CSV."

    if df.empty:

        return False, "CSV is empty."

    df = normalize_columns(df)

    timestamp = detect_timestamp_column(df)

    if timestamp is None:

        return False, "Timestamp column not found."

    return True, {

        "dataframe": df,

        "timestamp": timestamp

    }