from sqlalchemy import inspect
from app.extensions import db

def test_expected_tables_exist(app):
    with app.app_context():
        tables = set(inspect(db.engine).get_table_names())
        assert {"customers", "credit_reports", "risk_assessments", "audit_logs"} <= tables
