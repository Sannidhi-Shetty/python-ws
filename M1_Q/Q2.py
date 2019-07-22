"""a program to accept a number “n” from the user; then display the sum of the following series:"""
n=int(input("Enter the number:"))
sum=0
for i in range(1,n+1):
   sum+=1/i
print(f"The result is {sum}")