# Task15 - for_loop.py

This file contains multiple examples demonstrating Python `for` loops and related controls.

Examples in the file:

1. Basic loop
- Iterates over a list `fruits` and prints each item.

2. Loop through a string
- Iterates over each character in the string "Pakistan" and prints it.

3. `range()` example
- Uses `range(0, 21, 2)` to print even numbers from 0 to 20.

4. `break` example
- Iterates `fruits` and stops the loop when it encounters "apple" (so items after the break are not printed).

5. `continue` example
- Skips printing "apple" but continues the loop for remaining items.

6. `else` on a `for` loop
- The `else` block after a `for` runs only if the loop completes normally (no `break`).
- In this file the loop prints each fruit, and because no `break` occurs in that example, the `else` prints "Loop finished normally".
- If the loop used `break` and it executed, the `else` block would be skipped. If the iterable is empty, the `else` still runs (since no `break` happened).

7. `enumerate()` example
- Shows how to get both index and value when iterating a list.

8. Nested loops
- Uses nested `for` loops to print a small multiplication table (1 through 3).

## How to run

Run the script with Python:

```bash
python "Navtac Tasks/Task15/for_loop.py"
```
