from enum import Enum


class HealthStatus(Enum):
    """Health status enumeration for trees."""
    EXCELLENT = "excellent"
    GOOD = "good"
    FAIR = "fair"
    POOR = "poor"


def calculate_infrastructure_score(diameter: float, height: float, radius: float = 500) -> float:
    """
    Расчёт доступности инфраструктуры для дерева.
    
    Args:
        diameter (float): Диаметр ствола дерева (см)
        height (float): Высота дерева (м)
        radius (float): Радиус доступности инфраструктуры (м)
    
    Returns:
        float: Инфраструктурный скор (от 0.2 до 0.8)
    """
    if diameter > 30 and height > 10:
        score = 0.8
    elif diameter > 15:
        score = 0.5
    else:
        score = 0.2
    return score


def predict_growth(current_diameter: float, age: int, location: str = "park") -> float:
    """
    Прогнозирование роста дерева.
    
    Args:
        current_diameter (float): Текущий диаметр (см)
        age (int): Возраст дерева (лет)
        location (str): Тип посадки ("park" или "street")
    
    Returns:
        float: Прогнозируемый диаметр (см)
    """
    growth_factor = 1.15 if location == "park" else 1.05
    predicted = current_diameter * growth_factor * (1 + 0.02 * (10 - min(age, 10)))
    return round(predicted, 2)


def get_health_status(diameter: float, height: float, has_damage: bool = False) -> HealthStatus:
    """
    Определение состояния здоровья дерева.
    
    Args:
        diameter (float): Диаметр ствола дерева (см)
        height (float): Высота дерева (м)
        has_damage (bool): Есть ли видимые повреждения
    
    Returns:
        HealthStatus: Статус здоровья (EXCELLENT, GOOD, FAIR, POOR)
    """
    if has_damage:
        return HealthStatus.POOR
    elif diameter > 30 and height > 10:
        return HealthStatus.EXCELLENT
    elif diameter > 15:
        return HealthStatus.GOOD
    else:
        return HealthStatus.FAIR
    
