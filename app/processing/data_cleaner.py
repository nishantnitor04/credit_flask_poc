import pandas as pd

def clean_bureau_records(records):
    """Normalize optional bureau data before downstream analysis."""
    frame = pd.DataFrame(records)
    if frame.empty:
        return []
    frame = frame.drop_duplicates()
    frame = frame.where(pd.notnull(frame), None)
    return frame.to_dict(orient="records")
