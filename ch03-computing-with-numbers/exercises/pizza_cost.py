# 2 - pizza_cost.py
# Calculate the cost per square inch of a pizza

from math import pi


def area_circle(diameter: float) -> float:
    return pi * ((diameter / 2) ** 2)


def main() -> None:
    diameter = int(input("Diameter of pizza (in inches) > "))
    price = float(input("Price of pizza > "))
    area_of_pizza = area_circle(diameter)
    print(f"The cost per square inch of pizza is {price / area_of_pizza}")


if __name__ == "__main__":
    main()
