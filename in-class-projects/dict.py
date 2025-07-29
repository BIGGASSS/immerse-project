string = "hello"
dict = {}
for i in range(len(string)):
    dict[string[i]] = 0
for i in range(len(string)):
    dict[string[i]] += 1
print(dict)