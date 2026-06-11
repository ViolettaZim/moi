from pydantic import BaseModel, Field


class RuntimeConfig(BaseModel):
    """Dynamic configuration that can be updated via API."""

    log_level: str = Field(default="INFO", description="Logging level (INFO, DEBUG, WARNING, ERROR)")
    feature_flag: bool = Field(default=True, description="Enable experimental features")
    maintenance_mode: bool = Field(default=False, description="Enable maintenance mode")
    runtime_message: str = Field(default="System is operational", description="Custom runtime message")
    infrastructure_radius: int = Field(default=500, description="Default radius for infrastructure search (meters)")
    min_tree_diameter: float = Field(default=15.0, description="Minimum tree diameter for infrastructure consideration")

    class Config:
        json_schema_extra = {
            "example": {
                "log_level": "DEBUG",
                "feature_flag": True,
                "maintenance_mode": False,
                "runtime_message": "New runtime mode",
                "infrastructure_radius": 500,
                "min_tree_diameter": 15.0,
            }
        }
        
