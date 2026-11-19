import uuid
from .mock_responses import MOCK_BUREAU_DATA

class MockBureauClient:
    """Deterministic local substitute for an authorized credit bureau API."""

    def fetch_credit_report(self, customer):
        return {
            "bureau_reference": f"MOCK-{uuid.uuid4().hex[:12].upper()}",
            "credit_score": MOCK_BUREAU_DATA["credit_score"],
            "payment_history": MOCK_BUREAU_DATA["payment_history"],
            "credit_utilization": MOCK_BUREAU_DATA["credit_utilization"],
            "loan_history": MOCK_BUREAU_DATA["loan_history"],
            "customer_pan_last4": customer.pan_number[-4:],
            "provider": "MOCK_TRANSUNION",
        }
