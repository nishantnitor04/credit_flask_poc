# Credit Bureau Flask POC

## Request flow
Client -> Flask route -> controller/service -> repository -> SQLAlchemy -> PostgreSQL.

Credit-check flow:
1. Client authenticates using the POC login endpoint.
2. Client submits a customer ID to `/api/credit-check`.
3. Flask calls the local mock bureau adapter.
4. The report is stored in `credit_reports`.
5. Pandas calculates a demonstration risk score.
6. The assessment is stored in `risk_assessments`.
7. An audit event is recorded and the API returns both records.

## Important
The bureau integration and credit/risk formula are synthetic examples only.
They are not a real TransUnion API integration or a production credit-scoring model.
