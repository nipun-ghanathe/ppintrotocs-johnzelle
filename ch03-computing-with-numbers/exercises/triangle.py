# 9 - triangle.py
# Compute area of triangle given its sides

import math


def area_heron(a: float, b: float, c: float) -> float:
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def main() -> None:
    sides = map(
        float,
        input("enter sides of the triangle separated by commas (a,b,c) > ").split(","),
    )
    print(f"\narea of the triangle with given sides is {area_heron(*sides)}")


if __name__ == "__main__":
    main()
