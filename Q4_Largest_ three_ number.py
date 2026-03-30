#Q4A.
a = int(input("enter a number: "))
b = int(input("enter a number: "))
c = int(input("enter a number: "))

if a >= b:
    if a >= c:
        print(f"{a} is the largest number")
    else:
        print(f"{c} is the largest number")
else:
    if b >= c:
        print(f"{b} is the largest number")
    else:
        print(f"{c} is the largest number")


