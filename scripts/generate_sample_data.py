import json
from pathlib import Path

sample = [
    {"payment_history": 800, "credit_utilization": 700, "loan_history": 750},
    {"payment_history": 650, "credit_utilization": 620, "loan_history": 680},
    {"payment_history": 500, "credit_utilization": 550, "loan_history": 600},
]
Path("sample_risk_records.json").write_text(json.dumps(sample, indent=2))
print("Created sample_risk_records.json")
