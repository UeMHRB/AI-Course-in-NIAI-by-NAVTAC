import cmath

a,b,c = map(float, input("Enter the coefficients a, b, and c of the quadratic equation (ax^2 + bx + c = 0): ").split())

# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Calculate the two solutions using the quadratic formula
solution1 = (-b + cmath.sqrt(discriminant)) / (2*a)
solution2 = (-b - cmath.sqrt(discriminant)) / (2*a)

print(f"The solutions to the quadratic equation are: {solution1:.2f} and {solution2:.2f}")