num = input("please select a number: ")
a = []
count = 0
while len(a) <= int(num):
    count += 1
    a.append(count)
for item in a:
    if int(num) % item == 0:
        print(item)