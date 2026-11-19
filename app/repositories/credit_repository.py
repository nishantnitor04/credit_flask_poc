from ..extensions import db
from ..models import CreditReport, RiskAssessment

class CreditRepository:
    @staticmethod
    def create_report(data):
        report = CreditReport(**data)
        db.session.add(report)
        db.session.commit()
        return report

    @staticmethod
    def get_report(report_id):
        return db.session.get(CreditReport, report_id)

    @staticmethod
    def create_risk_assessment(data):
        assessment = RiskAssessment(**data)
        db.session.add(assessment)
        db.session.commit()
        return assessment
