#AQ3.	Write a program to find the largest of two numbers. Expected Output: 

num1= int(input("enter a number: "))
num2= int(input("enter a number: "))
if num1 > num2:
    print(f"{num1} is greater") 
elif num1 < num2:
    print(f"{num2} is greater")
else:
    print("Both the number are equal")