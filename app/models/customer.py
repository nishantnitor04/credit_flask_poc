from datetime import datetime, timezone
from ..extensions import db

class Customer(db.Model):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True, index=True)
    pan_number = db.Column(db.String(10), nullable=False, unique=True, index=True)
    created_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    credit_reports = db.relationship("CreditReport", back_populates="customer", cascade="all, delete-orphan")
    audit_logs = db.relationship("AuditLog", back_populates="customer", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "pan_number": self.pan_number,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }
