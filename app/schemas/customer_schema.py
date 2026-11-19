import re

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
PAN_RE = re.compile(r"^[A-Z]{5}[0-9]{4}[A-Z]$")

def validate_customer_payload(payload):
    if not isinstance(payload, dict):
        return None, {"body": "JSON object is required"}

    errors = {}
    name = payload.get("name")
    email = payload.get("email")
    pan_number = payload.get("pan_number")

    if not isinstance(name, str) or not name.strip():
        errors["name"] = "Name is required"
    elif len(name.strip()) > 120:
        errors["name"] = "Name must be at most 120 characters"

    if not isinstance(email, str) or not EMAIL_RE.match(email):
        errors["email"] = "A valid email is required"

    if not isinstance(pan_number, str) or not PAN_RE.match(pan_number.upper()):
        errors["pan_number"] = "PAN must match the format ABCDE1234F"

    if errors:
        return None, errors

    return {
        "name": name.strip(),
        "email": email.strip().lower(),
        "pan_number": pan_number.strip().upper(),
    }, None
