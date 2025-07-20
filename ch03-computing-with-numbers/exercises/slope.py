# 6 - slope.py
# Compute the slope of a line

from collections.abc import Iterable


def get_slope(pt1: Iterable[float | int], pt2: Iterable[float | int]) -> float:
    x1, y1 = pt1
    x2, y2 = pt2
    return (y2 - y1) / (x2 - x1)


def main() -> None:
    print("enter any two points on the line as x,y:")
    pt1 = map(int, input("first point > ").split(","))
    pt2 = map(int, input("second point > ").split(","))
    print(f"\nThe slope of the line is {get_slope(pt1, pt2):.1f}")


if __name__ == "__main__":
    main()
