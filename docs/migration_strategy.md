# Flask to FastAPI migration strategy

1. Freeze this Flask application as the baseline.
2. Capture representative API request/response fixtures.
3. Keep business rules and Pandas processing framework-independent.
4. Migrate HTTP routes and request/response validation to FastAPI/Pydantic.
5. Reuse/refactor SQLAlchemy models and repositories.
6. Continue managing the same database schema with Alembic.
7. Run shared business-rule tests and adapted API contract tests against both apps.
8. Compare database state, error behavior and performance under the same workload.

Do not run Flask and FastAPI schema creation independently against production.
Use reviewed Alembic revisions and backups for real environments.
