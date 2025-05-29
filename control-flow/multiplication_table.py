# Prompt the user for a number
number = int(input("Enter a number to see its multiplication table:"))

#Generate and Print the Multiplication Table
for i in range(1, 11):
    Z = number * i
    print(f"{number} * {i} = {Z}")
    
    
    