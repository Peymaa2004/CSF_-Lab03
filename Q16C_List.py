
numbers = [4, 9, 6, 10]
search = int(input("enter a number to search: "))
found = False
for num in numbers:
    if num == search:
        print("Number Found")
        found = True
if not found:
    print ("Number not found")
