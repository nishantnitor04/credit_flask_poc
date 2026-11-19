import pytest
from app.processing.credit_score_processor import normalize_credit_score

def test_normalize_credit_score():
    assert normalize_credit_score(755) == 755

def test_reject_out_of_range_score():
    with pytest.raises(ValueError):
        normalize_credit_score(950)
