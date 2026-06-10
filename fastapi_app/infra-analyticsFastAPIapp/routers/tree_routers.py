from typing import Optional

from fastapi import APIRouter, HTTPException, Query
from services.test_service import tree_service

tree_router = APIRouter(prefix="/trees", tags=["Trees"])


@tree_router.get("/health")
def health_check():
    """Проверка работоспособности API."""
    return {"status": "ok"}


@tree_router.get("/accessibility")
def tree_accessibility(
    diameter: float = Query(..., description="Диаметр ствола дерева (см)"),
    height: float = Query(..., description="Высота дерева (м)"),
    radius: float = Query(500, description="Радиус доступности инфраструктуры (м)"),
):
    """
    Расчёт доступности инфраструктуры для дерева.
    """
    return tree_service.calculate_infrastructure_score(diameter, height, radius)


@tree_router.get("/growth-prediction")
def predict_growth(
    current_diameter: float = Query(..., description="Текущий диаметр (см)"),
    age: int = Query(..., description="Возраст дерева (лет)"),
    location: str = Query("park", description="Тип локации (park/other)"),
):
    """Прогнозирование роста дерева."""
    return tree_service.predict_tree_growth(current_diameter, age, location)


@tree_router.get("/health-status")
def get_health_status(
    diameter: float = Query(..., description="Диаметр ствола дерева (см)"),
    height: float = Query(..., description="Высота дерева (м)"),
    has_damage: bool = Query(False, description="Наличие повреждений"),
):
    """Определение состояния здоровья дерева."""
    return tree_service.get_health_status(diameter, height, has_damage)


@tree_router.get("/execute")
def execute_operation(
    operation: str = Query(
        ..., description="Операция: calculate_score, predict_growth, get_health_status"
    ),
    diameter: float = Query(..., description="Диаметр ствола дерева (см)"),
    height: float = Query(..., description="Высота дерева (м)"),
    radius: float = Query(500, description="Радиус доступности инфраструктуры (м)"),
    current_diameter: Optional[float] = Query(
        None, description="Текущий диаметр для predict_growth"
    ),
    age: Optional[int] = Query(None, description="Возраст для predict_growth"),
    location: Optional[str] = Query("park", description="Локация для predict_growth"),
    has_damage: Optional[bool] = Query(
        False, description="Повреждения для get_health_status"
    ),
):

    try:
        if operation == "calculate_score":
            return tree_service.extract_operation(operation, diameter, height, radius)
        elif operation == "predict_growth":
            if current_diameter is None or age is None:
                raise HTTPException(
                    status_code=400,
                    detail="Для predict_growth нужны current_diameter и age",
                )
            return tree_service.extract_operation(
                operation, current_diameter, age, location
            )
        elif operation == "get_health_status":
            return tree_service.extract_operation(
                operation, diameter, height, has_damage
            )
        else:
            raise HTTPException(
                status_code=400, detail=f"Операция {operation} не поддерживается"
            )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
