from enum import Enum
from ..exceptions import InvalidTreeDataError, InvalidLocationError, InvalidRadiusError


class HealthStatus(Enum):
    """Health status enumeration for trees."""
    EXCELLENT = "excellent"
    GOOD = "good"
    FAIR = "fair"
    POOR = "poor"


def validate_tree_input(diameter: float, height: float) -> None:
    """Validate tree input parameters."""
    if diameter <= 0:
        raise InvalidTreeDataError(f"Diameter must be positive. Got: {diameter}")
    if height <= 0:
        raise InvalidTreeDataError(f"Height must be positive. Got: {height}")


def calculate_infrastructure_score(
    diameter: float, 
    height: float, 
    radius: float = 500
) -> float:
    """
    Calculate infrastructure accessibility score for a tree.
    
    Args:
        diameter: Tree trunk diameter (cm)
        height: Tree height (m)
        radius: Infrastructure search radius (m)
    
    Returns:
        float: Infrastructure score (0.2 to 0.8)
    """
    if radius <= 0:
        raise InvalidRadiusError(f"Radius must be positive. Got: {radius}")
    
    validate_tree_input(diameter, height)
    
    if diameter > 30 and height > 10:
        score = 0.8
    elif diameter > 15:
        score = 0.5
    else:
        score = 0.2
    return score


def predict_growth(
    current_diameter: float, 
    age: int, 
    location: str = "park"
) -> float:
    """
    Predict tree growth after 5 years.
    
    Args:
        current_diameter: Current diameter (cm)
        age: Tree age (years)
        location: Planting type ("park" or "street")
    
    Returns:
        float: Predicted diameter after 5 years (cm)
    """
    validate_tree_input(current_diameter, 1.0)
    
    if age <= 0:
        raise InvalidTreeDataError(f"Age must be positive. Got: {age}")
    
    if location not in ["park", "street"]:
        raise InvalidLocationError(f"Location must be 'park' or 'street'. Got: {location}")
    
    growth_factor = 1.15 if location == "park" else 1.05
    predicted = current_diameter * growth_factor * (1 + 0.02 * (10 - min(age, 10)))
    return round(predicted, 2)


def get_health_status(
    diameter: float, 
    height: float, 
    has_damage: bool = False
) -> HealthStatus:
    """
    Determine tree health status.
    
    Args:
        diameter: Tree trunk diameter (cm)
        height: Tree height (m)
        has_damage: Whether tree has visible damage
    
    Returns:
        HealthStatus: Health status (EXCELLENT, GOOD, FAIR, POOR)
    """
    validate_tree_input(diameter, height)
    
    if has_damage:
        return HealthStatus.POOR
    elif diameter > 30 and height > 10:
        return HealthStatus.EXCELLENT
    elif diameter > 15:
        return HealthStatus.GOOD
    else:
        return HealthStatus.FAIR
    
    
    
