# 10 - ladder.py
# Find length of ladder for reaching given height with given angle

from math import pi, sin


def main() -> None:
    height = float(input("enter the height to be reached (in meters) > "))
    # take angle in degrees and convert it into radians
    angle = float(
        input("enter the angle made by ladder with ground (in degrees) > ")
    ) * (pi / 180)
    ladder_length = height / sin(angle)
    print(f"\nThe length of the ladder should be {ladder_length:.2f}")


if __name__ == "__main__":
    main()
