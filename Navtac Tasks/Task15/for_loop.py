# 1. Basic loop
fruits = ["mango", "apple", "banana"]
for fruit in fruits:
    print(fruit)

# 2. Loop through string
for char in "Pakistan":
    print(char)

# 3. range() - print even numbers 0 to 20
for i in range(0, 21, 2):
    print(i)

# 4. break - stop when you find "apple"
for fruit in fruits:
    if fruit == "apple":
        break
    print(fruit)

# 5. continue - skip "apple"
for fruit in fruits:
    if fruit == "apple":
        continue
    print(fruit)

# 6. else - prints only if no break happened
for fruit in fruits:
    print(fruit)
else:
    print("Loop finished normally")

# 7. enumerate - show index + value
for i, fruit in enumerate(fruits):
    print(i, fruit)

# 8. Nested loop - multiplication table (1 to 3)
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")