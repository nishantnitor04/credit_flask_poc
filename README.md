**Purpose**
This is a Flask 3 proof-of-concept for a legacy credit-bureau workflow. It is also designed as a baseline for migrating to FastAPI.

The main workflow is:

Customer → mock bureau response → credit report → Pandas risk assessment → audit log

**Application structure**
app/init.py: Flask application factory.
app/config.py: Environment-based database, JWT, and bureau settings.
app/routes/: HTTP endpoints and JWT enforcement.
app/services/: Business orchestration.
app/repositories/: SQLAlchemy database operations.
app/models/: Database entities.
app/processing/: Pandas-based risk calculations.
app/integrations/transunion_mock/: Deterministic mock bureau adapter.
app/schemas/: Manual request validation.
tests/: Unit, API, integration, migration, regression, and performance tests.

**Database entities**
Customer: name, email, PAN, timestamps.
CreditReport: bureau reference, credit score, bureau attributes, raw JSON response.
RiskAssessment: one assessment per credit report.
AuditLog: success/failure credit-check events.
Relationships are implemented in app/models/customer.py, app/models/credit_report.py, app/models/risk_assessment.py, and app/models/audit_log.py.

**API flow**
Customer APIs
Registered under /api/customers:

POST /api/customers
GET /api/customers
GET /api/customers/{id}
The customer route validates name, email, and PAN format before calling the customer service. app/routes/customer_routes.py

**Authentication**
POST /api/auth/login accepts hardcoded POC credentials and returns a JWT:

Username: poc_user
Password: poc_password_change_me
Protected endpoints use @jwt_required().

See app/routes/auth_routes.py.

Credit check
POST /api/credit-check:

Validates customer_id.
Loads the customer.
Calls MockBureauClient.
Persists a CreditReport.
Calculates a risk score.
Persists a RiskAssessment.
Writes a success or failure audit record.
The transaction and rollback behavior live in app/services/credit_service.py.

GET /api/credit-reports/{id} retrieves a stored report and its optional assessment.

**Risk analysis**
POST /api/risk-analysis accepts a list of records and calculates:

Risk score = 40% payment history + 30% credit utilization + 30% loan history
LOW: score ≥ 750
MEDIUM: score ≥ 650
HIGH: below 650
See app/processing/pandas_processor.py.

**Health**
GET /health executes SELECT 1 to verify database connectivity.

**Persistence**
Default development storage is SQLite:
sqlite:///credit_bureau.db

Docker Compose provides PostgreSQL 16 with the application exposed on port 5000. The Compose startup runs:


Database configuration is in app/config.py, with deployment in docker-compose.yml.
flask db upgrade
python run.py

Important separation of concerns
Routes do HTTP validation and responses.
Services coordinate business operations.
Repositories interact with SQLAlchemy.

**How to run**
cd credit_bureau_flask_poc

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt

copy .env.example .env

flask db init
flask db migrate -m "initial schema"
flask db upgrade


python -m scripts.seed_database

python run.py

pytest -v
