# 8 - epact.py
# figure out epact

# C = year//100
# epact = (8 + (C // 4) - C + ((8C + 13) // 25) + 11 * (year % 19)) % 30


def get_epact(year: int) -> int:
    c = year // 100
    epact = (8 + (c // 4) - c + ((8 * c + 13) // 25) + 11 * (year % 19)) % 30
    return epact


def main() -> None:
    year = int(input("enter the year (YYYY) > "))
    print(f"\nThe value of the epact is {get_epact(year)}")


if __name__ == "__main__":
    main()
