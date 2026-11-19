def validate_credit_request(payload):
    if not isinstance(payload, dict):
        return None, {"body": "JSON object is required"}

    customer_id = payload.get("customer_id")
    if not isinstance(customer_id, int) or customer_id <= 0:
        return None, {"customer_id": "A positive integer customer_id is required"}

    return {"customer_id": customer_id}, None
