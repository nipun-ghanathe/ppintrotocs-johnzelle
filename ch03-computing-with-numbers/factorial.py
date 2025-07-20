# factorial.py
# Compute the factorial of a number


def factorial(n: int) -> int:
    return 1 if n in {0, 1} else n * factorial(n - 1)


def main() -> None:
    print("Enter 'q' at any time to quit.")

    while True:
        user_input = input("\nPlease enter a whole number > ")
        if user_input == "q":
            print("\nTerminating program...")
            break
        if not user_input.isdecimal():
            continue
        number = int(user_input)
        print(f"The factorial of {number} is {factorial(number)}")


if __name__ == "__main__":
    main()
