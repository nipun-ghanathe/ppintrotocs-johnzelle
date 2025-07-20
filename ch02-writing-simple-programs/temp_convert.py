# temp_convert.py
# A program to convert fahrenheit to celsius


def fahrenheit_to_celsius(f: float) -> float:
    return (f - 32) * (5 / 9)


def main() -> None:
    print("Welcome to temp_convert.py\nA program to convert fahrenheit to celsius.\n")
    fahrenheit = float(input("Enter temperature in fahrenheit: "))
    print(fahrenheit_to_celsius(fahrenheit))


if __name__ == "__main__":
    main()
