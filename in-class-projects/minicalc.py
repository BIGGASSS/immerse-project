def add(a: int, b: int):
    return a+b
def sub(a: int, b: int):
    return a-b
def mul(a: int, b: int):
    return a*b
def div(a: int, b: int):
    if b == 0:
        return "Cannot divide by zero!"
    else:
        return a/b

x = input("Select an operation(+-*/): ")
a = input("Input the first number: ")
b = input("input the second number: ")
a = int(a)
b = int(b)
if x == '+':
    print(add(a, b))
elif x == '-':
    print(sub(a, b))
elif x == '*':
    print(mul(a, b))
elif x == '/':
    print(div(a, b))
else:
    print("Please select a vaild operation!")