number = input("please select a number: ")
if int(number) % 2 == 0:
    print("this number is even")
if int(number) % 4 == 0:
    print("this number is a multiple of 4")
if int(number) % 2 != 0:
    print("this number is odd")

num = input("please select a number to check: ")
check = input("please select a number to divide by: ")

if int(num) % int(check) == 0:
    print("these numbers are evenly divisible")
else:
    print("not today, my friend")