from ..extensions import db
from ..models import AuditLog

def write_audit(customer_id, request_type, status, message=None):
    entry = AuditLog(
        customer_id=customer_id,
        request_type=request_type,
        status=status,
        message=message,
    )
    db.session.add(entry)
    db.session.commit()
    return entry
