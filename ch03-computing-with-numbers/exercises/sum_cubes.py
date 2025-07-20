# 12 - sum_cubes.py
# Compute the sum of cubes of first n natural numbers


def sum_cubes(n: int) -> int:
    return n**3 + sum_cubes(n - 1) if n not in {0, 1} else 1 if n == 1 else 0


def main() -> None:
    n = int(input("number of natural numbers whose cubes you want to sum > "))
    print(f"\nThe sum of cubes of first {n} natural numbers is {sum_cubes(n)}.")


if __name__ == "__main__":
    main()
