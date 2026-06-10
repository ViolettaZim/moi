from typing import Optional


class TreeInfraService:
    def __init__(self, api_client=None):
        self.operations = {
            "calculate_score": self.calculate_infrastructure_score,
            "predict_growth": self.predict_tree_growth,
            "get_health_status": self.get_health_status,
        }

    def extract_operation(self, operation: str, *args, **kwargs):
        """Извлечение и выполнение операции."""
        if operation not in self.operations:
            raise Exception(
                f"Operation '{operation}' not available. Available: {list(self.operations.keys())}"
            )
        else:
            return self.operations[operation](*args, **kwargs)

    def calculate_infrastructure_score(
        self, diameter: float, height: float, radius: float = 500
    ):
        """
        Расчёт доступности инфраструктуры для дерева.
        """
        if diameter > 30 and height > 10:
            score = 0.8
        elif diameter > 15:
            score = 0.5
        else:
            score = 0.2
        return {
            "diameter_cm": diameter,
            "height_m": height,
            "radius_m": radius,
            "infrastructure_score": score,
            "status": "good" if score > 0.5 else "needs_improvement",
        }

    def predict_tree_growth(
        self, current_diameter: float, age: int, location: str = "park"
    ):
        """
        Прогнозирование роста дерева.
        """
        growth_factor = 1.15 if location == "park" else 1.05
        predicted = current_diameter * growth_factor * (1 + 0.02 * (10 - min(age, 10)))
        return {
            "current_diameter_cm": current_diameter,
            "age_years": age,
            "location_type": location,
            "predicted_diameter_5years_cm": round(predicted, 2),
            "growth_rate_percent": round(
                (predicted - current_diameter) / current_diameter * 100, 2
            ),
        }

    def get_health_status(
        self, diameter: float, height: float, has_damage: bool = False
    ):
        """
        Определение состояния здоровья дерева.
        """
        if has_damage:
            health_score = 0.3
            status = "poor"
        elif diameter > 30 and height > 10:
            health_score = 0.9
            status = "excellent"
        elif diameter > 15:
            health_score = 0.7
            status = "good"
        else:
            health_score = 0.5
            status = "fair"

        return {
            "diameter_cm": diameter,
            "height_m": height,
            "has_damage": has_damage,
            "health_score": health_score,
            "health_status": status,
        }


tree_service = TreeInfraService()
