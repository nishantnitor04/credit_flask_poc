from sqlalchemy.exc import IntegrityError
from ..repositories.customer_repository import CustomerRepository

class DuplicateCustomerError(Exception):
    pass

class CustomerService:
    @staticmethod
    def create_customer(data):
        if CustomerRepository.get_by_email(data["email"]):
            raise DuplicateCustomerError("Email already exists")
        if CustomerRepository.get_by_pan(data["pan_number"]):
            raise DuplicateCustomerError("PAN already exists")
        try:
            return CustomerRepository.create(data)
        except IntegrityError:
            from ..extensions import db
            db.session.rollback()
            raise DuplicateCustomerError("Customer already exists")

    @staticmethod
    def get_customer(customer_id):
        return CustomerRepository.get_by_id(customer_id)

    @staticmethod
    def list_customers():
        return CustomerRepository.list_all()
