# 17 - guess_sqrt.py
# Guess the square root of a number x as x/2 and improve n times using Newton's method.

import math


def guess_sqrt(x: float, n: int) -> float:
    """Guess the square root of a number x as x/2 and improve n times using Newton's method.

    Args:
        x: the number whose square root we are finding
        n: number of times we are improving the guess
    """  # noqa: E501
    guess = x / 2
    for _ in range(n):
        guess = (guess + (x / guess)) / 2
    return guess


def main() -> None:
    x = float(input("enter the number whose square root you want > "))
    n = int(input("enter number of times to improve the guess > "))
    guessed_sqrt = guess_sqrt(x, n)
    actual_sqrt = math.sqrt(x)
    print(f"\nThe guessed square root is: {guessed_sqrt}")
    print(f"The actual square root is: {actual_sqrt}")
    print(f"The difference is: {actual_sqrt - guessed_sqrt}")


if __name__ == "__main__":
    main()
