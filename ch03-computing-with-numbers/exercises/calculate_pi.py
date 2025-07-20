# 15 - calculate_pi.py
# Find the value of pi using Leibniz Series (until n terms)
# Leibniz series:
# 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...

import math


def find_pi(n: int) -> float:
    approx_pi = 0
    for i in range(n):
        approx_pi += ((-1) ** i) * (4 / (2 * i + 1))
    return approx_pi


def main() -> None:
    n = int(input("number of terms you would like to go upto in leibniz series > "))
    approx_pi = find_pi(n)
    diff = math.pi - approx_pi
    print(f"\nThe value of pi found is {approx_pi}")
    print(f"The differnce of this value from actual value is {diff}")


if __name__ == "__main__":
    main()
