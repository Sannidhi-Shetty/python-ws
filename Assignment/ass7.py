"""program to accept a number from the user and determine the sum of digits of that number. Repeat the operation until the sum gets to be a single digit number."""
n=input("Enter a number:")
num = int(n)
while num//10 != 0:
    sum = 0
    for i in n:
        sum += int(i)
    n = str(sum)
    num = sum
print(num)
