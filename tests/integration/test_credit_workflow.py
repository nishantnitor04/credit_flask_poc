from app.models import CreditReport, RiskAssessment

def test_credit_workflow_persists_report_and_assessment(client, customer, auth_headers, app):
    response = client.post("/api/credit-check", json={"customer_id": customer}, headers=auth_headers)
    assert response.status_code == 200
    with app.app_context():
        assert CreditReport.query.count() == 1
        assert RiskAssessment.query.count() == 1
