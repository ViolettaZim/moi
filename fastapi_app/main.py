from __version__ import APP_VERSION
from fastapi import FastAPI
from routers.tree_routers import tree_router

app = FastAPI(
    version=APP_VERSION,
    title="Infra-analytics App",
    description="API для прогнозирования динамики роста городских зелёных насаждений",
)

app.include_router(tree_router)


@app.get("/")
def get_root():
    return {
        "status": "ok",
        "message": "Infra Analytics API for green infrastructure",
        "version": APP_VERSION,
        "endpoints": [
            "/trees/health",
            "/trees/accessibility",
            "/trees/growth-prediction",
            "/trees/health-status",
            "/trees/execute",
        ],
    }


@app.get("/health")
def health_check():
    """Health check для сервера."""
    return {"status": "healthy", "service": "green-infrastructure-analytics"}
