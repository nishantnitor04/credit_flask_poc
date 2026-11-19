from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token

auth_bp = Blueprint("auth", __name__)

# POC-only credentials. Replace with a persisted user model and password hashing.
POC_USERNAME = "poc_user"
POC_PASSWORD = "poc_password_change_me"

@auth_bp.post("/api/auth/login")
def login():
    payload = request.get_json(silent=True) or {}
    if payload.get("username") != POC_USERNAME or payload.get("password") != POC_PASSWORD:
        return jsonify({"error": {"code": "INVALID_CREDENTIALS", "message": "Invalid username or password"}}), 401
    token = create_access_token(identity=POC_USERNAME)
    return jsonify({"access_token": token, "token_type": "Bearer"}), 200
