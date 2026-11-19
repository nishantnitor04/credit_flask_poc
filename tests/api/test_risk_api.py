def test_risk_analysis(client, auth_headers):
    response = client.post("/api/risk-analysis", headers=auth_headers, json={
        "records": [{
            "payment_history": 800,
            "credit_utilization": 700,
            "loan_history": 750
        }]
    })
    assert response.status_code == 200
    assert response.get_json()["data"][0]["risk_score"] == 755.0

def test_risk_analysis_validation(client, auth_headers):
    response = client.post("/api/risk-analysis", headers=auth_headers, json={"records": []})
    assert response.status_code == 400
