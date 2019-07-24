"""6.	Write a program to find the sum of the given elements of the list."""
from functools import reduce
lst =[1,2,3,4,5,6,7,8,9]
res =reduce(lambda a,b:a+b,lst)
print(f"Sumof elements = {res}")