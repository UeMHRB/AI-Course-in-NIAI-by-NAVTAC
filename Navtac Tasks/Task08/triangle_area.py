a,b,c = map(float, input("Enter the lengths of the three sides of the triangle, separated by spaces: ").split())

s = (a + b + c) / 2 #semi pereimeter

area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

print(f"The area of the triangle with sides {a}, {b}, and {c} is: {area:.4f}")