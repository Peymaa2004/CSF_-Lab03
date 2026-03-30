
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Erroe: Division by zero"
# Menu-driven calculator
while True:
    print("\n1. Add")
    print("2. substract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = int(input("enter a choice: "))
    if choice == 5:
        print("Exiting Calculator....")
        break
    num1 = float(input("enter a first number: "))
    num2 = float(input("enter a second number: "))
    


