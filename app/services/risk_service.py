from ..processing.pandas_processor import calculate_risk

class RiskService:
    @staticmethod
    def analyze(records):
        return calculate_risk(records)
