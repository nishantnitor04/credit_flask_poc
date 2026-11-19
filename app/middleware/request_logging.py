import time
from flask import g, request, current_app

def register_request_logging(app):
    @app.before_request
    def start_timer():
        g.request_started_at = time.perf_counter()

    @app.after_request
    def log_request(response):
        elapsed_ms = (time.perf_counter() - getattr(g, "request_started_at", time.perf_counter())) * 1000
        current_app.logger.info(
            "method=%s path=%s status=%s duration_ms=%.2f",
            request.method, request.path, response.status_code, elapsed_ms
        )
        return response
