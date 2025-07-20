# convert2.py
# A program that prints a table of celsius to fahrenheit for first 10 multiples of 10


def convert_celsius_to_fahrenheit(celsius: float) -> float:
    fahrenheit = ((9 / 5) * celsius) + 32
    return fahrenheit


def main() -> None:
    print(
        "Printing table of celsius to fahrenheit mapping for first 10 multiples of 10:\n"
    )
    print("celsius".ljust(8) + " " + "fahrenheit".ljust(8))
    print("-" * 8 + " " + "-" * 8)
    for celsius in range(0, 101, 10):
        fahrenheit = convert_celsius_to_fahrenheit(celsius)
        print(f"{celsius:>8.2f} {fahrenheit:>8.2f}")


if __name__ == "__main__":
    main()
