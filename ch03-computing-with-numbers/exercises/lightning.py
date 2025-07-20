# 4 - lightning.py
# Compute distance to a lightning strike using time elapsed between viewing and hearing it

speed_of_sound = 343  # m/s


def main() -> None:
    time_delta = int(
        input("time elapsed between flash and sound of thunder (seconds) > ")
    )
    distance = speed_of_sound * time_delta
    print(f"The distance to the lightning strike is {distance:.2f}")


if __name__ == "__main__":
    main()
