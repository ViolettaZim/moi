def add_tree_metrics(diameter: float, height: float) -> float:
    """Рассчёт показателя здоровья дерева."""
    return diameter * height / 100


if __name__ == "__main__":
    diameter = 25.0
    height = 12.0
    result = add_tree_metrics(diameter, height)
    print(f"Диаметр: {diameter} см, Высота: {height} м")
    print(f"Показатель здоровья дерева: {result}")
