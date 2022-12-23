# Program to calculate average from user inputted numbers

# Create variable to store user inputted float
# Create variable to store the total and quantity of numbers
numbers = float(input("Please enter a number or -1 to exit: "))
total = 0
quantity = 0

# Using while loop with the condition that while the user does not enter -1 to avoid including -1
# in the equation, keep asking for the user for input and increment total and quantity variables
# with new value. If value meets the condition of user entering -1 then calculate average, display
# and exit loop
while numbers != -1:

    total += numbers
    quantity += 1
    numbers = float(input("Please enter a number or -1 to exit: "))

    if numbers == -1:
        average = total / quantity
        print(round(average, 2))
        break
