import random as rm
n=rm.randint(1,7)
print(n)
num=0
while True:
    m = int(input("Enter a  number to be guessed:"))

    if m==n:
        num +=1
        print("Correct guess")
        break
    elif m<n:
        print("The number is less than specified")
        num +=1
    else:
        print("The number is greater than specified")
        num +=1
    if num <3:
        print("Chance exceeded")