# 3 - cho_weight.py
# Compute the molecular weight of a carbohydrate


def main() -> None:
    carbon = int(input("number of carbon atoms > "))
    hydrogen = int(input("number of hydrogen atoms > "))
    oxygen = int(input("number of oxygen atoms > "))
    molecular_weight = carbon * 12 + hydrogen + oxygen * 16
    print(f"The molecular weight of given carbohydrate is {molecular_weight} u.")


if __name__ == "__main__":
    main()
