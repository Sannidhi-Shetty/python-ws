""" program to accept a number “n” from the user; then display the sum of the following series:"""
n=int(input("Enter the number:"))
sum=0
for i in range(2,n+1):
   sum+=1/i**3
print(f"The result is {sum}")