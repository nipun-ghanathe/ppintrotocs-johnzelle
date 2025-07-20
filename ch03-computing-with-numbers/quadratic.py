# quadratic.py
# A program that computes the real roots of quadratic equation.

import math


def get_discriminant(a: float, b: float, c: float) -> float:
    return (b**2 - 4 * a * c)  # fmt: skip


def roots_exist(discriminant: float) -> bool:
    return discriminant >= 0


def get_roots(a: float, b: float, c: float) -> tuple[float, float] | None:
    discriminant = get_discriminant(a, b, c)
    if not roots_exist(discriminant):
        return None
    disc_root = math.sqrt(discriminant)
    r1 = (-b + disc_root) / 2 * a
    r2 = (-b - disc_root) / 2 * a
    return (r1, r2)


def main() -> None:
    print("This program finds the real solutions to a quadratic.\n")
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    roots = get_roots(a, b, c)
    print()
    if roots:
        print(f"The roots are {roots[0]} and {roots[1]}")
    else:
        print("There are not real roots for given coefficients.")


if __name__ == "__main__":
    main()
