# futval.py
# A program to compute the value of an investment after certain years


def main():
    print("Calculate the compound interest using this program.\n")
    principal = int(input("Enter the initial amount: "))
    rate = int(input("Enter the annual rate of interest (in percentage): "))
    n = int(input("Enter the number of times the interest is compounded in a year: "))
    years = int(input("Enter the period of investment (years): "))
    print(
        f"\nThe final amount needed to pay is {principal * ((1 + rate / (n * 100)) ** (n * years)):.2f}"
    )


main()
