from ..models import RuntimeConfig


class RuntimeConfigService:
    """Singleton service for runtime configuration management."""

    _instance = None
    _config: RuntimeConfig = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._config = RuntimeConfig()
        return cls._instance

    def get_config(self) -> RuntimeConfig:
        """Get current runtime configuration."""
        return self._config

    def update_config(self, new_config: RuntimeConfig) -> RuntimeConfig:
        """Update runtime configuration."""
        self._config = new_config
        return self._config
    
    