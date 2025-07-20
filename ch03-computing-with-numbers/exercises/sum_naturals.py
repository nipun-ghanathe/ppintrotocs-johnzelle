# 11 - sum_naturals.py
# Compute the sum of first n natural numbers


def sum_naturals(n: int) -> int:
    return (n * (n + 1)) // 2


def main() -> None:
    n = int(input("enter the number of integers you want to sum > "))
    print(f"the sum of first {n} natural numbers is {sum_naturals(n)}")


if __name__ == "__main__":
    main()
