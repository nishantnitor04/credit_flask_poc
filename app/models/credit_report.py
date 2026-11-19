from datetime import datetime, timezone
from ..extensions import db

class CreditReport(db.Model):
    __tablename__ = "credit_reports"

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"), nullable=False, index=True)
    bureau_reference = db.Column(db.String(80), nullable=False, unique=True)
    credit_score = db.Column(db.Integer, nullable=False)
    payment_history = db.Column(db.Float, nullable=False)
    credit_utilization = db.Column(db.Float, nullable=False)
    loan_history = db.Column(db.Float, nullable=False)
    raw_response = db.Column(db.JSON, nullable=False)
    report_status = db.Column(db.String(30), nullable=False, default="COMPLETED")
    created_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    customer = db.relationship("Customer", back_populates="credit_reports")
    risk_assessment = db.relationship("RiskAssessment", back_populates="credit_report", uselist=False, cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "customer_id": self.customer_id,
            "bureau_reference": self.bureau_reference,
            "credit_score": self.credit_score,
            "payment_history": self.payment_history,
            "credit_utilization": self.credit_utilization,
            "loan_history": self.loan_history,
            "report_status": self.report_status,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }
