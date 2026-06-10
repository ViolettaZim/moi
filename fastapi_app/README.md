# infra-analyticsFastAPIapp

Библиотека для анализа зелёных насаждений и доступности инфраструктуры в городской среде.

## Описание

`infra-analyticsFastAPIapp` предоставляет инструменты для:
- Расчёта доступности инфраструктуры (полив, скамейки, освещение) вокруг деревьев
- Прогнозирования роста деревьев на основе возраста и местоположения
- Оценки состояния здоровья зелёных насаждений

Библиотека предназначена для использования в городских системах мониторинга и службах озеленения.

## Установка

```bash
pip install infra-analyticsFastAPIapp

Пример использования

from services.test_service import TreeInfraService

Создание экземпляра сервиса
service = TreeInfraService(api_client=None)

Расчёт срока для дерева
result = service.calculate_infrastructure_score(
    diameter=25.0,   # диаметр ствола (см)
    height=12.0,     # высота дерева (м)
    radius=500       # радиус доступности (м)
)
print(result)

Прогнозирование роста дерева
prediction = service.predict_tree_growth(
    current_diameter=20.0,  # текущий диаметр (см)
    age=15,                  # возраст дерева (лет)
    location="park"          # тип посадки: "park" или "street"
)
print(prediction)

Оценка здоровья дерева
health = service.get_health_status(
    diameter=18.0,      # диаметр (см)
    height=8.0,         # высота (м)
    has_damage=False    # наличие повреждений
)
print(health)

Результат выполнения
{
    "diameter_cm": 25.0,
    "height_m": 12.0,
    "radius_m": 500,
    "infrastructure_score": 0.5,
    "status": "needs_improvement"
}
