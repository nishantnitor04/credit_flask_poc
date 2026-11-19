def test_credit_check_requires_auth(client, customer):
    response = client.post("/api/credit-check", json={"customer_id": customer})
    assert response.status_code == 401

def test_credit_check_success(client, customer, auth_headers):
    response = client.post(
        "/api/credit-check",
        json={"customer_id": customer},
        headers=auth_headers
    )
    assert response.status_code == 200
    body = response.get_json()["data"]
    assert body["credit_report"]["credit_score"] == 755
    assert body["risk_assessment"]["risk_category"] == "LOW"

def test_credit_check_customer_not_found(client, auth_headers):
    response = client.post(
        "/api/credit-check",
        json={"customer_id": 999},
        headers=auth_headers
    )
    assert response.status_code == 404

def test_get_credit_report_not_found(client, auth_headers):
    response = client.get("/api/credit-reports/999", headers=auth_headers)
    assert response.status_code == 404
