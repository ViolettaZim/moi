import geopandas as gpd
from shapely.geometry import Point

from src.infra_analytics import (
    accessibility_ratio,
    count_within_radius,
    unserved_trees,
)


def main():
    trees = gpd.GeoDataFrame(
        {
            "id": [1, 2, 3, 4, 5],
            "species": ["Дуб", "Берёза", "Клён", "Сосна", "Липа"],
        },
        geometry=[
            Point(55.751244, 37.618423),
            Point(55.752244, 37.619423),
            Point(55.753244, 37.620423),
            Point(55.754244, 37.621423),
            Point(55.755244, 37.622423),
        ],
        crs="EPSG:4326",
    )

    infrastructure = gpd.GeoDataFrame(
        {
            "type": ["Полив", "Скамейка", "Освещение", "Полив", "Скамейка"],
        },
        geometry=[
            Point(55.751500, 37.618500),
            Point(55.752500, 37.619500),
            Point(55.753500, 37.620500),
            Point(55.754500, 37.621500),
            Point(55.755500, 37.622500),
        ],
        crs="EPSG:4326",
    )

    radius = 500

    print("=" * 60)
    print("ЛАБОРАТОРНАЯ РАБОТА №3")
    print("Библиотека: infra_analytics")
    print("Тема: Анализ доступности инфраструктуры для зелёных насаждений")
    print("=" * 60)

    print("\n1. ПРИМЕР: count_within_radius()")
    print("-" * 40)
    result = count_within_radius(trees, infrastructure, radius)
    print("Результат:")
    print(result[["id", "species", "infrastructure_count"]])

    print("\n2. ПРИМЕР: unserved_trees()")
    print("-" * 40)
    unserved = unserved_trees(trees, infrastructure, radius)
    if len(unserved) > 0:
        print(f"Деревья без инфраструктуры в радиусе {radius}м:")
        print(unserved[["id", "species"]])
    else:
        print(f"Все деревья обеспечены инфраструктурой в радиусе {radius}м")

    print("\n3. ПРИМЕР: accessibility_ratio()")
    print("-" * 40)
    ratio = accessibility_ratio(trees, infrastructure, radius)
    print(f"Доля деревьев с доступной инфраструктурой: {ratio:.2%}")

    print("\n" + "=" * 60)
    print("Все примеры успешно выполнены!")
    print("=" * 60)


if __name__ == "__main__":
    main()

    