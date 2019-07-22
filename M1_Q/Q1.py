#Write a progr1.	Write a program to accept a number and determine whether it is a prime number or not.
#am to accept a number and determine whether it is a prime number or not.
def is_prime(N):
 if N<2:
  return False
 else:
  for i in range(2,N//2+1):
   if N % i ==0:
     return False
   return True
N=int(input("Enter a number:"))
if is_prime(N):
 print(f"{N} is prime")
else:
 print(f"{N} is not prime")


