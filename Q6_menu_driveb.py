#Q6A

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("enter a chpoice: "))
num1 = float(input("enter a first number: "))
num2 = float(input("enter a second number: "))

if choice == 1:
    print("sum =", num1 = num2)
elif choice == 2:
    print("Difference =", num1 - num2)
elif choice == 3:
    print ("product =", num1 * num2)
elif choice == 4:
    if num2 != 0:
        print("Quotient +", num1 / num2)
    else:
        print("Erroe: Division by zero")

else:
    print("Invalid Choice")