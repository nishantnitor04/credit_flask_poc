def normalize_credit_score(score):
    if isinstance(score, bool) or not isinstance(score, (int, float)):
        raise ValueError("Credit score must be numeric")
    if score < 300 or score > 900:
        raise ValueError("Credit score must be between 300 and 900")
    return int(score)
