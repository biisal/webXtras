import os
from contextlib import asynccontextmanager

from loguru import logger
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from fastapi.openapi.utils import get_openapi

from app.config import (
    DOWNLOADS_DIR,
    APP_CONFIG_DOCS_URL,
    APP_CONFIG_OPENAPI_URL,
    API_CONFIG_ALLOW_ORIGIN,
)

from app.image_processing.router import router as image_processing_router
from app.pdf_processing.router import router as pdf_processing_router


def app_factory(app):
    if not os.path.exists(DOWNLOADS_DIR):
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)

    allow_origins = [
        origin.strip() for origin in API_CONFIG_ALLOW_ORIGIN.split(",")
    ]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=allow_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    ### CUSTOM ROUTES
    app.include_router(
        router=image_processing_router, prefix="/api/image", tags=["Image Processing"]
    )
    app.include_router(
        router=pdf_processing_router, prefix="/api/pdf", tags=["PDF Processing"]
    )

    return app

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("For setting up database connection and migrations")
    yield

app = FastAPI(
    title="WebXtras Automation Tools API",
    description="An API for the WebXtras Tools Project",
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
    openapi_url=APP_CONFIG_OPENAPI_URL,
    docs_url=APP_CONFIG_DOCS_URL,
    lifespan=lifespan,
    version="0.1.0",
)

app = app_factory(app)

# --------------------------------------------------------------------------
# Protecting fastapi /doc, /redoc and openapi.json endpoints
# --------------------------------------------------------------------------

@app.get("/api", include_in_schema=False)
async def root():
    return {"message": "WebXtras Api Endpoints"}

@app.get("/api/openapi.json", include_in_schema=False)
async def openapi():
    return get_openapi(title=app.title, version=app.version, routes=app.routes)


@app.get("/api/docs", include_in_schema=False)
async def get_swagger_documentation():
    return get_swagger_ui_html(openapi_url="/api/openapi.json", title="docs")


@app.get("/api/redoc", include_in_schema=False)
async def get_redoc_documentation():
    return get_redoc_html(openapi_url="/api/openapi.json", title="docs")


# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
