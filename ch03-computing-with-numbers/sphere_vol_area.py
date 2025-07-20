# sphere_vol_area.py
# Computes volume and surface area of a sphere

from math import pi


def volume_sphere(radius: float) -> float:
    return (4 / 3) * pi * (radius**3)


def surface_area_sphere(radius: float) -> float:
    return 4 * pi * (radius**2)


def main():
    radius = int(input("Enter radius of the sphere > "))
    print()
    print(f"The volume of the sphere is {volume_sphere(radius):.2f}")
    print(f"The surface area of the sphere is {surface_area_sphere(radius):.2f}")


if __name__ == "__main__":
    main()
