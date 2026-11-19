def test_create_customer(client):
    response = client.post("/api/customers", json={
        "name": "Asha Verma",
        "email": "asha@example.com",
        "pan_number": "PQRSX1234A"
    })
    assert response.status_code == 201
    assert response.get_json()["data"]["email"] == "asha@example.com"

def test_create_customer_validation_error(client):
    response = client.post("/api/customers", json={"name": "Asha"})
    assert response.status_code == 400
    assert response.get_json()["error"]["code"] == "VALIDATION_ERROR"

def test_list_customers(client, customer):
    response = client.get("/api/customers")
    assert response.status_code == 200
    assert len(response.get_json()["data"]) == 1

def test_get_customer_not_found(client):
    response = client.get("/api/customers/999")
    assert response.status_code == 404

def test_duplicate_customer(client, customer):
    response = client.post("/api/customers", json={
        "name": "Another Name",
        "email": "rahul@example.com",
        "pan_number": "ZZZZZ9999Z"
    })
    assert response.status_code == 409
