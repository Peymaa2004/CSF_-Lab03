# Integrated Program

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
#Functioonto print no. from 1 to 10 with even or odd
def print_numbers(n):
    for i in range(1, n + 1):
        print(f"{i} -> {check_even_odd(i)}")
# Input from user
n = int(input("enter a n: "))
print_numbers(n)