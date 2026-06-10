from pydantic import BaseModel, Field
from typing import Literal

class RuntimeConfigModel(BaseModel):
    """Runtime configuration model (for responses)."""

    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR"] = Field(
        default="INFO", description="Logging level"
    )
    feature_flag: bool = Field(default=True, description="Enable experimental features")
    maintenance_mode: bool = Field(default=False, description="Enable maintenance mode")
    runtime_message: str = Field(default="System is operational", description="Custom runtime message")
    infrastructure_radius: int = Field(default=500, description="Default radius for infrastructure search (meters)")
    min_tree_diameter: float = Field(default=15.0, description="Minimum tree diameter for infrastructure consideration")

    class Config:
        json_schema_extra = {
            "example": {
                "log_level": "INFO",
                "feature_flag": True,
                "maintenance_mode": False,
                "runtime_message": "System is operational",
                "infrastructure_radius": 500,
                "min_tree_diameter": 15.0,
            }
        }

class RuntimeConfigUpdateModel(BaseModel):
    """Runtime configuration update model (for PUT requests)."""

    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR"] = Field(
        default="INFO", description="Logging level"
    )
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

        