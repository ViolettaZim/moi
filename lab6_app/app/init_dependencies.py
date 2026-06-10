from .config import app_config as static_config
from .schemas.app_config import AppConfigModel
from .schemas.runtime_config import RuntimeConfigModel
from .services.runtime_config_service import RuntimeConfigService


class DependenciesContainer(dict):
    """Custom dictionary for dependency injection."""

    def get(self, key: str, default=None):
        """Safely get a dependency by key."""
        return super().get(key, default)


def init_dependencies() -> DependenciesContainer:
    """Initialize all dependencies and return the container."""

    # Create static config model
    static_config_model = AppConfigModel(
        app_name=static_config.app_name,
        app_version=static_config.app_version,
        app_description=static_config.app_description,
        app_authors=static_config.app_authors,
        contact_email=static_config.contact_email,
        license_name=static_config.license_name,
    )

    # Create runtime config model
    runtime_config_model = RuntimeConfigModel(
        log_level="INFO",
        feature_flag=True,
        maintenance_mode=False,
        runtime_message="System is operational",
        infrastructure_radius=500,
        min_tree_diameter=15.0,
    )

    # Create runtime config service
    runtime_config_service = RuntimeConfigService()
    runtime_config_service.initialize(runtime_config_model)

    # Return container
    return DependenciesContainer({
        "app_config": static_config_model,
        "runtime_config_service": runtime_config_service,
    })



