list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []
odds = []

leng = len(list)
for i in range(leng):
    if list[i] % 2 == 0:
        evens.append(list[i])
    else:
        odds.append(list[i])

print("Even numbers:")
print(evens)
print("Odd numbers:")
print(odds)