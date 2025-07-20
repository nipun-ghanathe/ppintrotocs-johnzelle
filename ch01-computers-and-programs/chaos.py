# chaos.py
# A simple program illustrating chaotic behaviour.
# ie. a small change in input leading to huge changes in result
# you can check the result for inputs 0.25 and 0.26


def main():
    print("This program illustrates a chaotic function.")
    x = float(input("Enter a number between 0 and 1: "))
    print(f"\ninput  {x:.2f}")
    print("-" * 12)
    for _ in range(20):
        x = 3.9 * x * (1 - x)
        print(f"{x:>11.2f}")


if __name__ == "__main__":
    main()
