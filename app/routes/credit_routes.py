from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from ..schemas.credit_schema import validate_credit_request
from ..services.customer_service import CustomerService
from ..services.credit_service import CreditService

credit_bp = Blueprint("credit", __name__)

@credit_bp.post("/credit-check")
@jwt_required()
def credit_check():
    payload, errors = validate_credit_request(request.get_json(silent=True))
    if errors:
        return jsonify({"error": {"code": "VALIDATION_ERROR", "details": errors}}), 400

    customer = CustomerService.get_customer(payload["customer_id"])
    if not customer:
        return jsonify({"error": {"code": "CUSTOMER_NOT_FOUND", "message": "Customer not found"}}), 404

    try:
        report, assessment = CreditService().run_credit_check(customer)
    except Exception:
        return jsonify({"error": {"code": "BUREAU_PROCESSING_ERROR", "message": "Credit bureau processing failed"}}), 502

    return jsonify({
        "data": {
            "credit_report": report.to_dict(),
            "risk_assessment": assessment.to_dict()
        }
    }), 200

@credit_bp.get("/credit-reports/<int:report_id>")
@jwt_required()
def get_credit_report(report_id):
    report = CreditService.get_report(report_id)
    if not report:
        return jsonify({"error": {"code": "CREDIT_REPORT_NOT_FOUND", "message": "Credit report not found"}}), 404
    result = {"credit_report": report.to_dict()}
    if report.risk_assessment:
        result["risk_assessment"] = report.risk_assessment.to_dict()
    return jsonify({"data": result}), 200
