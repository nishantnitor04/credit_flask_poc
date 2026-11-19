from app.processing.pandas_processor import calculate_risk

def test_reference_calculation_is_stable():
    # Keep this golden test unchanged during the framework migration.
    inputs = [{
        "payment_history": 800,
        "credit_utilization": 700,
        "loan_history": 750
    }]
    result = calculate_risk(inputs)
    assert result == [{
        "payment_history": 800,
        "credit_utilization": 700,
        "loan_history": 750,
        "risk_score": 755.0,
        "risk_category": "LOW"
    }]
