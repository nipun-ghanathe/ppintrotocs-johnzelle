# 7 - distance.py
# Compute distance between two points

import math
from collections.abc import Iterable


def get_distance(pt1: Iterable[float | int], pt2: Iterable[float | int]) -> float:
    x1, y1 = pt1
    x2, y2 = pt2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def main() -> None:
    print("enter the two points in the form x,y:")
    pt1 = map(int, input("first point > ").split(","))
    pt2 = map(int, input("second point > ").split(","))
    print(f"\nThe distance between the points is {get_distance(pt1, pt2):.1f}")


if __name__ == "__main__":
    main()
