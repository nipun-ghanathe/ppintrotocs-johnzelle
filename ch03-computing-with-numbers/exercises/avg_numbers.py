# 14 - avg_numbers.py
# Compute average of numbers provided by the user


def main() -> None:
    n = int(input("How many numbers do you want to average? "))
    print()
    sum_numbers = 0
    for _ in range(n):
        sum_numbers += int(input("next number > "))
    print(f"\nThe average of the numbers you provided is {sum_numbers / n:.2f}")


if __name__ == "__main__":
    main()
