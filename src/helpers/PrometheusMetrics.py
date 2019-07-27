from flask import request
from prometheus_client import Counter, Histogram
import time
import sys

SERVER_APP_NAME = 'server'
REQUEST_COUNT = Counter('request_count', 'API Request Count', ['app_name', 'method', 'endpoint', 'http_status'])
REQUEST_LATENCY = Histogram('request_latency_seconds', 'API Request latency', ['app_name', 'endpoint'])

def startTimer():
    request.start_time = time.time()

def stopTimer(response):
    responseTime = time.time() - request.start_time
    REQUEST_LATENCY.labels(SERVER_APP_NAME, request.path).observe(responseTime)
    sys.stderr.write(f"{responseTime}\n")
    REQUEST_COUNT.labels(SERVER_APP_NAME, request.method, request.path, response.status_code).inc()
    return response

def setupMetrics(app):
    app.before_request(startTimer)
    app.after_request(stopTimer)