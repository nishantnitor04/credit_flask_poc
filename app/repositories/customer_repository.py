from ..extensions import db
from ..models import Customer

class CustomerRepository:
    @staticmethod
    def create(data):
        customer = Customer(**data)
        db.session.add(customer)
        db.session.commit()
        return customer

    @staticmethod
    def get_by_id(customer_id):
        return db.session.get(Customer, customer_id)

    @staticmethod
    def get_by_email(email):
        return Customer.query.filter_by(email=email).first()

    @staticmethod
    def get_by_pan(pan_number):
        return Customer.query.filter_by(pan_number=pan_number).first()

    @staticmethod
    def list_all():
        return Customer.query.order_by(Customer.id.asc()).all()
