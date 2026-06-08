from src.infra_analytics.core.tree_metrics import (
    calculate_infrastructure_score,
    get_health_status,
    predict_growth,
)


def main():
    """Example of tree infrastructure analysis."""
    try:
        score = calculate_infrastructure_score(25.0, 12.0)
        print(f"Infrastructure score: {score}")

        predicted = predict_growth(20.0, 15, "park")
        print(f"Predicted growth after 5 years: {predicted} cm")

        health = get_health_status(25.0, 12.0, False)
        print(f"Health status: {health.value}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
