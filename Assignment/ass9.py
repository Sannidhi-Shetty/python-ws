"""a program to accept a five-digit number, increment each digit by 1 and then display the new number formed. Note that digit 9 gets incremented to 0."""
inp = input("Enter a string:")
res = ' '
for i in inp:
    temp = int(i)
    temp =(temp+1)%10
    res += str(temp)

print(res)

