import os

DOWNLOADS_DIR = os.getenv("DOWNLOADS_DIR", "shared/downloads")

API_CONFIG_ALLOW_ORIGIN = os.getenv("API_CONFIG_ALLOW_ORIGIN", "*")

APP_CONFIG_DOCS_URL = os.getenv("APP_CONFIG_DOCS_URL", "/api/docs")

APP_CONFIG_OPENAPI_URL = os.getenv(
    "APP_CONFIG_OPENAPI_URL", "/api/openapi.json"
)