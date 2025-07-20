# dist_convert.py
# A program to convert kilometers to miles


def kilometers_to_miles(km: float) -> float:
    return km * 0.62


def main() -> None:
    print("Welcome to dist_convert.py\nA program to convert kilometers to miles.\n")
    km = float(input("Enter the distance in kilometers: "))
    print(kilometers_to_miles(km))


if __name__ == "__main__":
    main()
