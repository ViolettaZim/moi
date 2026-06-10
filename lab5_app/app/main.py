from contextlib import asynccontextmanager

from app.config import app_config
from app.routes import router
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application lifecycle (startup and shutdown events)."""
    print(f"Starting {app_config.app_name} v{app_config.app_version}")
    print(f"{app_config.app_description}")

    yield


app = FastAPI(
    title=app_config.app_name,
    version=app_config.app_version,
    description=app_config.app_description,
    contact={"email": app_config.contact_email} if app_config.contact_email else None,
    license_info={"name": app_config.license_name} if app_config.license_name else None,
    lifespan=lifespan,
)

app.include_router(router)


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": f"Welcome to {app_config.app_name}",
        "version": app_config.app_version,
        "docs_url": "/docs",
    }
