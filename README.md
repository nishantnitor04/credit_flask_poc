# Credit Bureau Flask POC

A runnable Flask 3 reference application intended to be the legacy source for a later FastAPI migration.

## Included
- Flask application factory and Blueprints
- Customer CRUD (create, list, get)
- SQLAlchemy 2.x models and relationships
- Flask-Migrate / Alembic configuration
- JWT login for protected demo endpoints
- Pandas-based synthetic risk calculation
- Local mock credit-bureau adapter
- Audit logging and health endpoint
- Pytest unit, API, integration, migration-smoke and regression tests
- Docker Compose with PostgreSQL

## 1. Create environment

Python 3.12 is recommended.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

Copy `.env.example` to `.env` and update secrets. SQLite is the default for a quick local run.

## 2. Initialize database migrations

```bash
flask db init
flask db migrate -m "initial credit bureau schema"
flask db upgrade
```

The `migrations/` directory is included as the location for generated Alembic revisions. The first migration revision is generated in your environment using the installed dependency versions.

Seed a demo customer:

```bash
python scripts/seed_database.py
```

## 3. Run the Flask app

```bash
python run.py
```

Base URL: `http://localhost:5000`

## 4. Try the API

### Health
```bash
curl http://localhost:5000/health
```

### Create customer
```bash
curl -X POST http://localhost:5000/api/customers \
  -H "Content-Type: application/json" \
  -d '{"name":"Rahul Sharma","email":"rahul@example.com","pan_number":"ABCDE1234F"}'
```

### Login and get JWT
```bash
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"poc_user","password":"poc_password_change_me"}'
```

Copy `access_token` from the response.

### Run credit check
```bash
curl -X POST http://localhost:5000/api/credit-check \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d '{"customer_id":1}'
```

### Run risk analysis
```bash
curl -X POST http://localhost:5000/api/risk-analysis \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d '{"records":[{"payment_history":800,"credit_utilization":700,"loan_history":750}]}'
```

## 5. Run tests

```bash
pytest -v
pytest --cov=app --cov-report=term-missing
```

## 6. Run with PostgreSQL using Docker

```bash
docker compose up --build
```

The API is exposed on port 5000 and PostgreSQL on port 5432. For a production-quality Compose setup, add a database health check and wait-for-ready behavior before running migrations.

## API endpoints

| Method | Endpoint | Auth |
|---|---|---|
| POST | `/api/auth/login` | No |
| POST | `/api/customers` | No (POC) |
| GET | `/api/customers` | No (POC) |
| GET | `/api/customers/{id}` | No (POC) |
| POST | `/api/credit-check` | JWT |
| GET | `/api/credit-reports/{id}` | JWT |
| POST | `/api/risk-analysis` | JWT |
| GET | `/health` | No |

## POC-only security notes

- Demo login credentials are hardcoded. Do not use this authentication implementation outside a local demonstration.
- Change all secrets before use.
- PAN is sensitive personal data. This sample stores synthetic PAN-like values in plaintext for demonstration only. A real system needs consent, encryption/tokenization, masking, access controls, retention rules and audit controls.
- The mock bureau adapter returns deterministic synthetic values. It does not contact TransUnion.
- The weighted Pandas score is illustrative only and is not a validated lending or credit decision model.
- Do not send real customer data to this POC.

## Migration notes

This app intentionally keeps Pandas processing, services, repositories and SQLAlchemy models outside the Flask routes. That separation makes them easier to reuse when the HTTP layer is migrated to FastAPI.
