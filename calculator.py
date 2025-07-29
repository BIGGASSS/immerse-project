x = input("Enter your first number: ")
y = input("Enter your second number: ")
x = int(x)
y = int(y)
print("You entered:", x, y)
print("The sum is:", x + y)
print("The product is:", x * y)
print("The difference is:", x - y)
if y == 0:
    print("Cannot divide by zero!")
else: 
    print("The quotient is:", x / y)