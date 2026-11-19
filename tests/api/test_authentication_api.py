def test_login_success(client):
    response = client.post("/api/auth/login", json={
        "username": "poc_user",
        "password": "poc_password_change_me"
    })
    assert response.status_code == 200
    assert "access_token" in response.get_json()

def test_login_invalid_credentials(client):
    response = client.post("/api/auth/login", json={
        "username": "wrong",
        "password": "wrong"
    })
    assert response.status_code == 401
