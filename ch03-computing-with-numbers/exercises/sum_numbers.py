# 13 - sum_numbers.py
# Compute sum of numbers provided by the user


def main() -> None:
    n = int(input("How many numbers do you want to sum? "))
    print()
    sum_numbers = 0
    for _ in range(n):
        sum_numbers += int(input("next number > "))
    print(f"\nThe sum of the numbers you provided is {sum_numbers}")


if __name__ == "__main__":
    main()
