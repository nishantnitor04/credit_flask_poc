import pandas as pd

REQUIRED_COLUMNS = ["payment_history", "credit_utilization", "loan_history"]

def calculate_risk(records):
    """Calculate a weighted risk score using a DataFrame.

    This example uses synthetic bureau attributes, not a real credit-scoring model.
    """
    if not records:
        raise ValueError("At least one record is required")

    df = pd.DataFrame(records)
    missing = [column for column in REQUIRED_COLUMNS if column not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")

    for column in REQUIRED_COLUMNS:
        df[column] = pd.to_numeric(df[column], errors="raise")
        if ((df[column] < 0) | (df[column] > 1000)).any():
            raise ValueError(f"{column} must be between 0 and 1000")

    df["risk_score"] = (
        df["payment_history"] * 0.40
        + df["credit_utilization"] * 0.30
        + df["loan_history"] * 0.30
    ).round(2)

    df["risk_category"] = df["risk_score"].apply(
        lambda score: "LOW" if score >= 750
        else "MEDIUM" if score >= 650
        else "HIGH"
    )
    return df.to_dict(orient="records")
