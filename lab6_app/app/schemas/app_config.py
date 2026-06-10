from pydantic import BaseModel, Field

class AppConfigModel(BaseModel):
    """Static configuration that only changes on app restart."""

    app_name: str = Field(default="Green Infrastructure API", description="Application name")
    app_version: str = Field(default="0.1.0", description="Application version")
    app_description: str = Field(
        default="API for analyzing infrastructure accessibility for green spaces (trees)",
        description="Application description"
    )
    app_authors: list[str] = Field(default=["ViolettaZim"], description="List of authors")
    contact_email: str = Field(default="viozim@ya.ru", description="Contact email")
    license_name: str = Field(default="MIT", description="License name")

    class Config:
        json_schema_extra = {
            "example": {
                "app_name": "Green Infrastructure API",
                "app_version": "0.1.0",
                "app_description": "API for analyzing infrastructure accessibility for green spaces (trees)",
                "app_authors": ["ViolettaZim"],
                "contact_email": "viozim@ya.ru",
                "license_name": "MIT",
            }
        }

        