"""Pydantic models for API responses."""

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    """Response model for health check endpoint."""

    status: str = Field(default="ok", description="Health status")

    class Config:
        json_schema_extra = {"example": {"status": "ok"}}


class ErrorResponse(BaseModel):
    """Response model for error responses."""

    detail: str = Field(..., description="Error message")

    