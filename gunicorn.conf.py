import logging
import multiprocessing
import os

WORKERS = os.getenv("WORKERS", multiprocessing.cpu_count() * 2 + 1)
TIMEOUT = os.getenv("APPLICATION_TIMEOUT", 30)
BIND_PORT = os.getenv("PORT", 8000)
BIND_HOST = os.getenv("BIND", "0.0.0.0")
LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")

logging.basicConfig(level=LOG_LEVEL)
logger = logging.getLogger("GUNICORN_CONFIGURATION")
logger.info("APPLICATION_WORKERS: %s", WORKERS)
logger.info("APPLICATION_TIMEOUT: %s", TIMEOUT)
logger.info("APPLICATION_BIND: %s", f"{BIND_HOST}:{BIND_PORT}")
logger.info("APPLICATION_LOG_LEVEL: %s", LOG_LEVEL)

bind = f"{BIND_HOST}:{BIND_PORT}"
workers = WORKERS
timeout = TIMEOUT
graceful_timeout = 30
accesslog = "-"
errorlog = "-"
loglevel = LOG_LEVEL
worker_class = "uvicorn.workers.UvicornWorker"
