from flask import Blueprint, jsonify, request
from ..schemas.customer_schema import validate_customer_payload
from ..services.customer_service import CustomerService, DuplicateCustomerError

customer_bp = Blueprint("customers", __name__)

@customer_bp.post("")
def create_customer():
    data, errors = validate_customer_payload(request.get_json(silent=True))
    if errors:
        return jsonify({"error": {"code": "VALIDATION_ERROR", "details": errors}}), 400
    try:
        customer = CustomerService.create_customer(data)
        return jsonify({"data": customer.to_dict()}), 201
    except DuplicateCustomerError as exc:
        return jsonify({"error": {"code": "DUPLICATE_CUSTOMER", "message": str(exc)}}), 409

@customer_bp.get("")
def list_customers():
    customers = CustomerService.list_customers()
    return jsonify({"data": [customer.to_dict() for customer in customers]}), 200

@customer_bp.get("/<int:customer_id>")
def get_customer(customer_id):
    customer = CustomerService.get_customer(customer_id)
    if not customer:
        return jsonify({"error": {"code": "CUSTOMER_NOT_FOUND", "message": "Customer not found"}}), 404
    return jsonify({"data": customer.to_dict()}), 200
