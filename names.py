# Program to ask user to enter the names of students and enter stop to list all students
# create a variable names to store an empty string as initial value is empty
names = ""

""" While loop: As long as it stays true, keep asking user for input stored in a variable 'name'
and append to variable "names". If 'stop' is entered, print all 'names' and exit loop
"""

# Initial total of names is 0 which will append until user types stop
total_names = 0

while True:
    name = input("Enter the names of students else type stop to list all students: ")

    if name == "stop":
        break

    names += f"{name}\n"
    total_names += 1

print(names, end="")
print(f"Total number of students is {total_names}")