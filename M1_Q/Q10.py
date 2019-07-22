"""a program to print a pattern"""
for i in range(1,5+1):
    res =''
    for j in range(i-1,1):
        res +=' *'
        for k in range(1,i):
            res+=i
print(res)