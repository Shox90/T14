number = int(input("Enter a number: "))
i = 1
# (Thought process)
# Initial number is 1
# e.g. user enters 10, 20
# from 1+1 =2
# 2%2=0
# print(num)
# is number <= 10/20 etc.?
# do loop again
# else stop

while i <= number:
    if i % 2 == 0:
        print(i)
    i = i + 1