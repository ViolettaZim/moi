from src.infra_analytics.core.tree_metrics import (
    calculate_infrastructure_score,
    predict_growth,
    get_health_status,
)


def main():
    """Demo of tree infrastructure analysis."""
    print("=" * 60)
    print("Tree Infrastructure Analysis - Demo")
    print("=" * 60)

    test_cases = [
        {"diameter": 35.0, "height": 12.0, "age": 20, "location": "park", "has_damage": False},
        {"diameter": 20.0, "height": 8.0, "age": 10, "location": "street", "has_damage": False},
        {"diameter": 10.0, "height": 4.0, "age": 5, "location": "park", "has_damage": True},
        {"diameter": 25.0, "height": 11.0, "age": 15, "location": "street", "has_damage": False},
    ]

    for i, tree in enumerate(test_cases, 1):
        print(f"\n--- Tree {i} ---")
        print(f"Diameter: {tree['diameter']} cm, Height: {tree['height']} m")
        print(f"Age: {tree['age']} years, Location: {tree['location']}")
        print(f"Has damage: {tree['has_damage']}")

        try:
            score = calculate_infrastructure_score(tree['diameter'], tree['height'])
            print(f"Infrastructure score: {score}")

            predicted = predict_growth(tree['diameter'], tree['age'], tree['location'])
            print(f"Predicted diameter after 5 years: {predicted} cm")

            health = get_health_status(tree['diameter'], tree['height'], tree['has_damage'])
            print(f"Health status: {health.value}")

        except Exception as e:
            print(f"Error: {e}")

    print("\n" + "=" * 60)
    print("Demo completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()

    