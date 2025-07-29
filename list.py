list = [1, 10, 9, 8, 7, 6, 5, 4, 3, 2]
x = 0
n = len(list)
for i in range (n):
    x += list[i]
print("Sum:", x)
x = 1
for i in range (n):
    x *= list[i]
print("Product:", x)