from ..extensions import db
from ..models import CreditReport
from ..repositories.credit_repository import CreditRepository
from ..repositories.audit_repository import write_audit
from ..integrations.transunion_mock.client import MockBureauClient
from ..processing.pandas_processor import calculate_risk

class CreditService:
    def __init__(self, bureau_client=None):
        self.bureau_client = bureau_client or MockBureauClient()

    def run_credit_check(self, customer):
        try:
            bureau_data = self.bureau_client.fetch_credit_report(customer)
            report = CreditRepository.create_report({
                "customer_id": customer.id,
                "bureau_reference": bureau_data["bureau_reference"],
                "credit_score": bureau_data["credit_score"],
                "payment_history": bureau_data["payment_history"],
                "credit_utilization": bureau_data["credit_utilization"],
                "loan_history": bureau_data["loan_history"],
                "raw_response": bureau_data,
                "report_status": "COMPLETED",
            })
            result = calculate_risk([{
                "payment_history": report.payment_history,
                "credit_utilization": report.credit_utilization,
                "loan_history": report.loan_history,
            }])[0]
            assessment = CreditRepository.create_risk_assessment({
                "credit_report_id": report.id,
                "risk_score": result["risk_score"],
                "risk_category": result["risk_category"],
            })
            write_audit(customer.id, "CREDIT_CHECK", "SUCCESS", "Mock bureau report processed")
            return report, assessment
        except Exception:
            db.session.rollback()
            write_audit(customer.id, "CREDIT_CHECK", "FAILED", "Credit check processing failed")
            raise

    @staticmethod
    def get_report(report_id):
        return CreditRepository.get_report(report_id)
