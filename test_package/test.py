def calculate_infrastructure_score(
    diameter: float, height: float, radius: float = 500
) -> float:
    """
    Рассчёт доступности инфраструктуры для дерева.

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
    Прогнозирование роста дерева через 5 лет.

    Args:
        current_diameter (float): Текущий диаметр (см)
        age (int): Возраст дерева (лет)
        location (str): Тип посадки ("park" или "street")

    Returns:
        float: Прогнозируемый диаметр через 5 лет (см)
    """
    growth_factor = 1.15 if location == "park" else 1.05
    predicted = current_diameter * growth_factor * (1 + 0.02 * (10 - min(age, 10)))
    return round(predicted, 2)


def get_health_status(diameter: float, height: float, has_damage: bool = False) -> str:
    """
    Определение состояния здоровья дерева.

    Args:
        diameter (float): Диаметр ствола дерева (см)
        height (float): Высота дерева (м)
        has_damage (bool): Есть ли видимые повреждения

    Returns:
        str: Статус здоровья ("excellent", "good", "fair", "poor")
    """
    if has_damage:
        return "poor"
    elif diameter > 30 and height > 10:
        return "excellent"
    elif diameter > 15:
        return "good"
    else:
        return "fair"
