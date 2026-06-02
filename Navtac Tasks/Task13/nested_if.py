i = int(input("Enter a number: "))

if i == 10:
    print("i is equal to 10")
    print("First if statement is true")
    if i < 15:
        print("i is smaller than 15")
        print("Second nested if statement will excecute if the first if statement is true and this condition is also true")
    if i < 12:
        print("i is smaller than 12 too")
        print("Third nested if statement will execute if the first if statement is true and this condition is also true")
    else:
        print("i is greater than 15")
else:
    print("i is not equal to 10")
    
