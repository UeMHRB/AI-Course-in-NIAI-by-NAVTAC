import math

x = float(input("Enter a number to find its square root: "))

if x < 0:
    print("Cannot compute the square root of a negative number.")
else:
    sqrt_x = math.sqrt(x)
    print(f"The square root of {x} is approximately {sqrt_x:.4f}.")