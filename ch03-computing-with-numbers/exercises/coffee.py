# 5 - coffee.py
# Compute cost of a coffee


def get_order_cost(pounds_of_coffee: float) -> float:
    return ((10.5 + 0.86) * pounds_of_coffee) + 1.5


def main() -> None:
    pounds_of_coffee = int(input("pounds of coffees ordered > "))
    order_cost = get_order_cost(pounds_of_coffee)
    print(f"order cost is ${order_cost}")


if __name__ == "__main__":
    main()
