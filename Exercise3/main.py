
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for item in a:
    if item < 5:
        print(item)

b = []
for item in a:
    if item < 5:
        b.append(item)
print(b)

print([item for item in a if item < 5])
num = input("please select a number: ")
b2 = [item for item in a if item < int(num)]
print(b2)
