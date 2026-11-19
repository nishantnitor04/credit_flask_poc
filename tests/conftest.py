import pytest
from app import create_app
from app.extensions import db
from app.models import Customer

class TestConfig:
    TESTING = True
    SECRET_KEY = "test-secret"
    JWT_SECRET_KEY = "test-jwt-secret"
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_ACCESS_TOKEN_EXPIRES = False
    BUREAU_MODE = "mock"

@pytest.fixture()
def app():
    app = create_app(TestConfig)
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def customer(app):
    with app.app_context():
        item = Customer(name="Rahul Sharma", email="rahul@example.com", pan_number="ABCDE1234F")
        db.session.add(item)
        db.session.commit()
        return item.id

@pytest.fixture()
def auth_headers(client):
    response = client.post("/api/auth/login", json={
        "username": "poc_user",
        "password": "poc_password_change_me"
    })
    token = response.get_json()["access_token"]
    return {"Authorization": f"Bearer {token}"}
