import pytest
from app.processing.pandas_processor import calculate_risk

def test_calculate_risk_low():
    result = calculate_risk([{
        "payment_history": 800,
        "credit_utilization": 700,
        "loan_history": 750
    }])
    assert result[0]["risk_score"] == 755.0
    assert result[0]["risk_category"] == "LOW"

def test_calculate_risk_medium():
    result = calculate_risk([{
        "payment_history": 650,
        "credit_utilization": 650,
        "loan_history": 650
    }])
    assert result[0]["risk_category"] == "MEDIUM"

def test_calculate_risk_high():
    result = calculate_risk([{
        "payment_history": 500,
        "credit_utilization": 500,
        "loan_history": 500
    }])
    assert result[0]["risk_category"] == "HIGH"

def test_calculate_risk_empty_records():
    with pytest.raises(ValueError):
        calculate_risk([])

def test_calculate_risk_missing_column():
    with pytest.raises(ValueError, match="Missing required columns"):
        calculate_risk([{"payment_history": 700}])
