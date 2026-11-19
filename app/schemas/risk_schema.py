REQUIRED_FIELDS = ("payment_history", "credit_utilization", "loan_history")

def validate_risk_payload(payload):
    if not isinstance(payload, dict):
        return None, {"body": "JSON object is required"}

    rows = payload.get("records")
    if not isinstance(rows, list) or not rows:
        return None, {"records": "A non-empty list of records is required"}

    cleaned = []
    errors = {}
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            errors[str(index)] = "Each record must be a JSON object"
            continue
        item = {}
        for field in REQUIRED_FIELDS:
            value = row.get(field)
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                errors[f"{index}.{field}"] = "Must be a number"
            elif value < 0 or value > 1000:
                errors[f"{index}.{field}"] = "Must be between 0 and 1000"
            else:
                item[field] = float(value)
        cleaned.append(item)

    if errors:
        return None, errors
    return cleaned, None
