from prometheus_client import Counter, Histogram

REQUEST_COUNT = Counter("ai_service_requests_total", "Total API requests", ["endpoint", "method", "status"])
REQUEST_LATENCY = Histogram("ai_service_request_latency_seconds", "Request latency seconds", ["endpoint"])
