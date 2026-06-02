# Task 9: Quadratic Equation Solver

This file explains what `quadratic_eq.py` does.

## What `quadratic_eq.py` does
- Prompts the user to enter the coefficients `a`, `b`, and `c` of a quadratic equation (ax² + bx + c = 0).
- Calculates the discriminant: `discriminant = b² - 4ac`.
- Computes the roots using the quadratic formula:
  - `x1 = (-b + √discriminant) / (2a)`
  - `x2 = (-b - √discriminant) / (2a)`
- Displays the solutions to the user.

## Notes
- The script is intended for interactive use.
- It handles both real and complex roots depending on the discriminant value.
- Input values are converted to numeric form before calculation.
