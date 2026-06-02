# Task 8: Triangle Area Calculator

This file explains what `triangle_area.py` does.

## What `triangle_area.py` does
- Prompts the user to enter the three sides of a triangle: `a`, `b`, and `c`.
- Calculates the semi-perimeter `s = (a + b + c) / 2`.
- Uses Heron's formula to compute the triangle area:
  `area = (s * (s - a) * (s - b) * (s - c)) ** 0.5`
- Displays the computed area to the user.

## Notes
- The script is intended for interactive use.
- It converts input values to numeric form before calculation.
- This formula works for any valid triangle side lengths.
