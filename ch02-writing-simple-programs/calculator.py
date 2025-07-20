# calculator.py
# An interactive calculator program


def main() -> None:
    print("caculator\nAn interactive calculator program.\n")
    print("Enter 'q' at any time to quit.\n")

    while True:
        user_input = input("expression > ")
        if user_input == "q":
            print("\nProgram Terminating...")
            break
        print(eval(user_input), "\n")  # noqa: S307


if __name__ == "__main__":
    main()
