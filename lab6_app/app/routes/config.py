from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import get_app_config, get_runtime_config_service
from ..schemas.app_config import AppConfigModel
from ..schemas.responses import HealthResponse
from ..schemas.runtime_config import RuntimeConfigModel, RuntimeConfigUpdateModel
from ..services.runtime_config_service import RuntimeConfigService

router = APIRouter(prefix="/config", tags=["Configuration"])


@router.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """
    Health check endpoint.
    Returns application status.
    """
    return HealthResponse(status="ok")


@router.get("/app", response_model=AppConfigModel)
async def get_static_config(
    app_config: AppConfigModel = Depends(get_app_config),
) -> AppConfigModel:
    """
    Get static application configuration.
    These settings only change on application restart.
    """
    return app_config


@router.get("/runtime", response_model=RuntimeConfigModel)
async def get_runtime_config(
    runtime_service: RuntimeConfigService = Depends(get_runtime_config_service),
) -> RuntimeConfigModel:
    """
    Get current runtime configuration.
    These settings can be updated without restarting the application.
    """
    return runtime_service.get_config()


@router.put("/runtime", response_model=RuntimeConfigModel)
async def update_runtime_config(
    new_config: RuntimeConfigUpdateModel,
    runtime_service: RuntimeConfigService = Depends(get_runtime_config_service),
) -> RuntimeConfigModel:
    """
    Update runtime configuration.
    Changes apply immediately without restarting the application.
    """
    try:
        updated_config = runtime_service.update_config(new_config)
        return updated_config
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to update configuration: {str(e)}")
    
    