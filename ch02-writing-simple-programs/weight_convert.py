# weight_convert.py
# A program to convert kilograms to gram


def main() -> None:
    kg = float(input("Enter weight in kilograms: "))
    print(f"The weight in grams is: {kg * 1000:.1f}")


if __name__ == "__main__":
    main()
