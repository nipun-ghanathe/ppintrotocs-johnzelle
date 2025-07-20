# 16 - fibonacci.py
# Find the nth fibonacci term


def fibonacci(n: int) -> int:
    return 1 if n in {1, 2} else fibonacci(n - 1) + fibonacci(n - 2)


def main() -> None:
    n = int(input("which term of the fibonacci sequence do you want? "))
    print(f"\nterm on position {n} in fibonacci sequence is: '{fibonacci(n)}'")


if __name__ == "__main__":
    main()
