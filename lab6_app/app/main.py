import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from .dependencies import set_container
from .init_dependencies import init_dependencies
from .routes.config import router as config_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    container = init_dependencies()
    set_container(container)

    print("=" * 60)
    print("Starting Green Infrastructure API")
    print("=" * 60)

    app_config = container.get("app_config")
    print(f"App Name: {app_config.app_name}")
    print(f"Version: {app_config.app_version}")
    print(f"Description: {app_config.app_description}")
    print(f"Authors: {', '.join(app_config.app_authors)}")
    print("=" * 60)

    yield

    print("Shutting down Green Infrastructure API")


app = FastAPI(
    title=os.getenv("APP_NAME", "Green Infrastructure API"),
    version=os.getenv("APP_VERSION", "1.0.0"),
    description=os.getenv("APP_DESCRIPTION", "API for analyzing infrastructure accessibility for green spaces (trees)"),
    lifespan=lifespan,
)

app.include_router(config_router)


@app.get("/")
async def root():
    return RedirectResponse(url="/docs")


@app.get("/ping")
async def ping():
    return {"message": "pong"}



