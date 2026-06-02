# Task13 - `nested_if.py`

This file contains a Python program that demonstrates nested `if` statements.

## What the code does

- It asks the user to enter a number and stores it in the variable `i`.
- It checks whether `i` is equal to `10`.
- If `i` is equal to `10`, it prints:
  - `"i is equal to 10"`
  - `"First if statement is true"`
- Inside that first `if` block, it has two nested conditions:
  - If `i` is less than `15`, it prints two messages showing the second nested `if` executed.
  - If `i` is less than `12`, it prints two messages showing the third nested `if` executed.
  - Otherwise, it prints `"i is greater than 15"` for the third nested `if`'s `else` branch.
- If `i` is not equal to `10`, it prints `"i is not equal to 10"`.

## Important detail

Because the outer condition requires `i == 10`, the nested conditions only run when the entered number is exactly `10`.
