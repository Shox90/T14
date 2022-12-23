# Program to calculate average from 
numbers = float(input("Please enter a number or -1 to exit: "))
total = 0
count = 0

while numbers != -1:

    total += numbers
    count += 1
    numbers = float(input("Please enter a number or -1 to exit: "))

    if numbers == -1:
        average = total/count
        print(round(average, 2))
        break
