from ..extensions import db

def commit_or_rollback():
    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise
