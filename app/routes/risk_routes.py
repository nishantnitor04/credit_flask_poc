from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from ..schemas.risk_schema import validate_risk_payload
from ..services.risk_service import RiskService

risk_bp = Blueprint("risk", __name__)

@risk_bp.post("/risk-analysis")
@jwt_required()
def risk_analysis():
    records, errors = validate_risk_payload(request.get_json(silent=True))
    if errors:
        return jsonify({"error": {"code": "VALIDATION_ERROR", "details": errors}}), 400
    try:
        results = RiskService.analyze(records)
    except (ValueError, TypeError) as exc:
        return jsonify({"error": {"code": "RISK_ANALYSIS_ERROR", "message": str(exc)}}), 400
    return jsonify({"data": results}), 200
