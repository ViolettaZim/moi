from fastapi import Request

from .init_dependencies import DependenciesContainer
from .schemas.app_config import AppConfigModel
from .services.runtime_config_service import RuntimeConfigService


# Store the container instance
_container: DependenciesContainer = None


def set_container(container: DependenciesContainer) -> None:
    """Set the dependencies container."""
    global _container
    _container = container


def get_app_config() -> AppConfigModel:
    """Dependency provider for static application configuration."""
    if _container is None:
        raise RuntimeError("Dependencies container not initialized")
    return _container.get("app_config")


def get_runtime_config_service() -> RuntimeConfigService:
    """Dependency provider for runtime configuration service."""
    if _container is None:
        raise RuntimeError("Dependencies container not initialized")
    return _container.get("runtime_config_service")

