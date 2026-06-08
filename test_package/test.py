"""Test module - re-exports functions from core."""

from src.infra_analytics.core.tree_metrics import (
    HealthStatus,
    calculate_infrastructure_score,
    get_health_status,
    predict_growth,
)
