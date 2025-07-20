# convert.py
# A program to convert celsius temperature to fahrenheit


def main() -> None:
    print("Enter temperature in celsius and get it converted to fahrenheit.")
    print("Enter 'q' at any time to quit.")

    while True:
        input_string: str = input("\nWhat is the Celsius temperature? ")
        if input_string == "q":
            print("\nProgram Terminating...")
            break
        celsius: float = float(input_string)
        fahrenheit = ((9 / 5) * celsius) + 32
        print(f"The temperature is {fahrenheit} degree Fahrenheit.")

    print("\nProgram terminated.")


main()
