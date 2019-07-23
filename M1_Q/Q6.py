"""a program to accept a number from the user; then display the reverse of the entered number."""
N = int(input("Enter any number:"))
print(str(N)[::-1])
rev = 0
temp = N
while temp>0:
  rev = rev*10+(temp%10)
  temp = temp//10
print(rev)