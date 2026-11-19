from app import create_app
from app.extensions import db
from app.models import Customer

app = create_app()
with app.app_context():
    db.create_all()  # Convenience for local demo only; use Flask-Migrate for managed environments.
    if not Customer.query.filter_by(email="rahul@example.com").first():
        db.session.add(Customer(
            name="Rahul Sharma",
            email="rahul@example.com",
            pan_number="ABCDE1234F",
        ))
        db.session.commit()
    print("Database seeded. Demo customer: rahul@example.com / ABCDE1234F")
