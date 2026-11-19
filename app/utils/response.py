def success(data, status=200):
    return {"data": data}, status

def failure(code, message, status=400, details=None):
    error = {"code": code, "message": message}
    if details is not None:
        error["details"] = details
    return {"error": error}, status
