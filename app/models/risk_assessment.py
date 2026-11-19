from datetime import datetime, timezone
from ..extensions import db

class RiskAssessment(db.Model):
    __tablename__ = "risk_assessments"

    id = db.Column(db.Integer, primary_key=True)
    credit_report_id = db.Column(db.Integer, db.ForeignKey("credit_reports.id"), nullable=False, unique=True)
    risk_score = db.Column(db.Float, nullable=False)
    risk_category = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    credit_report = db.relationship("CreditReport", back_populates="risk_assessment")

    def to_dict(self):
        return {
            "id": self.id,
            "credit_report_id": self.credit_report_id,
            "risk_score": self.risk_score,
            "risk_category": self.risk_category,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }
