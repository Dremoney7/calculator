"""Solve quadratic equations of the form ax^2 + bx + c = 0."""

import cmath
import math


def solve_quadratic(a, b, c):
    """Return the roots of ax^2 + bx + c = 0.

    Real roots are returned as floats, complex roots as complex numbers.
    Raises ValueError if a == 0 (not a quadratic).
    """
    if a == 0:
        raise ValueError("Coefficient 'a' must be non-zero for a quadratic equation.")

    discriminant = b * b - 4 * a * c

    if discriminant > 0:
        sqrt_d = math.sqrt(discriminant)
        # Numerically stable form avoids cancellation when b is large
        q = -0.5 * (b + math.copysign(sqrt_d, b))
        return tuple(sorted((q / a, c / q)))
    if discriminant == 0:
        return (-b / (2 * a),)

    sqrt_d = cmath.sqrt(discriminant)
    return ((-b + sqrt_d) / (2 * a), (-b - sqrt_d) / (2 * a))


def main():
    print("Solve ax^2 + bx + c = 0")
    try:
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
        roots = solve_quadratic(a, b, c)
    except ValueError as e:
        print(f"Error: {e}")
        return

    if len(roots) == 1:
        print(f"One repeated real root: x = {roots[0]}")
    elif all(isinstance(r, float) for r in roots):
        print(f"Two real roots: x1 = {roots[0]}, x2 = {roots[1]}")
    else:
        print(f"Two complex roots: x1 = {roots[0]}, x2 = {roots[1]}")


if __name__ == "__main__":
    main()
