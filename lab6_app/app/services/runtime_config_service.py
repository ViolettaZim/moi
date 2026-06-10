from ..schemas.runtime_config import RuntimeConfigModel, RuntimeConfigUpdateModel


class RuntimeConfigService:
    """Singleton service for runtime configuration management."""

    _instance = None
    _config: RuntimeConfigModel = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def initialize(self, initial_config: RuntimeConfigModel) -> None:
        """Initialize the service with initial configuration."""
        self._config = initial_config.model_copy(deep=True)

    def get_config(self) -> RuntimeConfigModel:
        """Get current runtime configuration."""
        return self._config

    def update_config(self, new_config: RuntimeConfigUpdateModel) -> RuntimeConfigModel:
        """Update runtime configuration."""
        self._config = RuntimeConfigModel(**new_config.model_dump())
        return self._config
    
    