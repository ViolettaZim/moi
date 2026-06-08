"""Tree metrics calculation module."""

from enum import Enum

from ..exceptions import InvalidLocationError, InvalidRadiusError, InvalidTreeDataError


class HealthStatus(Enum):
    """Health status of a tree."""

    EXCELLENT = "excellent"
    GOOD = "good"
    FAIR = "fair"
    POOR = "poor"


def calculate_infrastructure_score(
    diameter: float, height: float, radius: float = 500
) -> float:
    """
    Calculate infrastructure score for a tree.

    Args:
        diameter: Diameter at breast height (cm)
        height: Tree height (m)
        radius: Infrastructure radius (m)

    Returns:
        Infrastructure score (0-1)
    """
    if diameter <= 0 or height <= 0:
        raise InvalidTreeDataError(
            f"Invalid tree data: diameter={diameter}, height={height}"
        )

    if radius <= 0:
        raise InvalidRadiusError(f"Invalid radius: {radius}")

    if diameter > 30 and height > 10:
        score = 0.8
    elif diameter > 15:
        score = 0.5
    else:
        score = 0.2

    return score


def predict_growth(current_diameter: float, age: int, location: str = "park") -> float:
    """
    Predict tree growth after 5 years.

    Args:
        current_diameter: Current diameter (cm)
        age: Tree age (years)
        location: Location type (park/other)

    Returns:
        Predicted diameter after 5 years (cm)
    """
    if current_diameter <= 0:
        raise InvalidTreeDataError(f"Invalid diameter: {current_diameter}")

    if age <= 0:
        raise InvalidTreeDataError(f"Invalid age: {age}")

    if location not in ["park", "other"]:
        raise InvalidLocationError(f"Invalid location: {location}")

    growth_factor = 1.15 if location == "park" else 1.05
    predicted = current_diameter * growth_factor * (1 + 0.02 * (10 - min(age, 10)))

    return round(predicted, 2)


def get_health_status(
    diameter: float, height: float, has_damage: bool = False
) -> HealthStatus:
    """
    Get tree health status.

    Args:
        diameter: Diameter at breast height (cm)
        height: Tree height (m)
        has_damage: Whether tree has visible damage

    Returns:
        HealthStatus enum value
    """
    if diameter <= 0 or height <= 0:
        raise InvalidTreeDataError(
            f"Invalid tree data: diameter={diameter}, height={height}"
        )

    if has_damage:
        return HealthStatus.POOR
    elif diameter > 30 and height > 10:
        return HealthStatus.EXCELLENT
    elif diameter > 15:
        return HealthStatus.GOOD
    else:
        return HealthStatus.FAIR
