from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from .green_zones.router import router as green_zones_router

app = FastAPI(
    title="Green Infrastructure API",
    description="CRUD service for green zones and metrics",
    version="0.1.0",
)

app.include_router(green_zones_router)

@app.get("/")
async def root():
    return RedirectResponse(url="/docs")

@app.get("/health")
def health_check():
    return {"status": "ok"}
