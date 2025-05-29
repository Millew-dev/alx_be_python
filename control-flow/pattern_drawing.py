# Prompt user for pattern size
size = int(input("Enter the size of the pattern:"))

#Validate the input
while size <= 0:
    print("Please enter a positive integer.")
    size = int(input("Enter the size of the pattern:"))


#Draw the pattern
row = 0
while row < size:
    for col in range(size):
        print("*", end="")
    #Move to the next line
    print()
    #Incremenet row counter
    row += 1