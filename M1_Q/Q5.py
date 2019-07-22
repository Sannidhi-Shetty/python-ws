""" program to print the Fibonacci series up to the number 34. """
n=34
a=0
b=1
print(a,b,end= " ")
for i in range(b,34):
    c=a+b
    print(c,end=" ")
    a=b
    b=c
    if c==34:
       break