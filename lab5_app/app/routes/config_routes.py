from fastapi import APIRouter, HTTPException

from ..config import app_config
from ..models import RuntimeConfig
from ..services import RuntimeConfigService

router = APIRouter(prefix="/config", tags=["Configuration"])
config_service = RuntimeConfigService()


@router.get("/health")
async def health_check():
    """
    Health check endpoint.
    Returns application status.
    """
    return {"status": "ok", "message": "Application is running"}


@router.get("/app")
async def get_static_config():
    """
    Get static application configuration.
    These settings only change on application restart.
    """
    return app_config.to_dict()


@router.get("/runtime")
async def get_runtime_config():
    """
    Get current runtime configuration.
    These settings can be updated without restarting the application.
    """
    return config_service.get_config().model_dump()


@router.put("/runtime")
async def update_runtime_config(new_config: RuntimeConfig):
    """
    Update runtime configuration.
    Changes apply immediately without restarting the application.
    """
    try:
        updated_config = config_service.update_config(new_config)
        return {
            "status": "success",
            "message": "Runtime configuration updated successfully",
            "config": updated_config.model_dump(),
        }
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to update configuration: {str(e)}"
        )
