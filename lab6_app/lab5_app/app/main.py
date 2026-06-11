from fastapi import FastAPI

from .config import app_config
from .routes import router

app = FastAPI(
    title=app_config.app_name,
    version=app_config.app_version,
    description=app_config.app_description,
    contact={"email": app_config.contact_email} if app_config.contact_email else None,
    license_info={"name": app_config.license_name} if app_config.license_name else None,
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


@app.on_event("startup")
async def startup_event():
    """Actions to perform on application startup."""
    print(f"Starting {app_config.app_name} v{app_config.app_version}")
    print(f"{app_config.app_description}")

    