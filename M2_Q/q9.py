"""9.	Write a program to find the word(s) that occur maximum and minimum number of times in the given paragraph. Also, display those words next to their respective count."""
inp="Comprehensions are a feature of Python which I would really miss if I ever have to leave it. Comprehensions are constructs that allow sequences to be built from other sequences. Several types of comprehensions are supported in both Python 2 and Python 3."""
lst=[]
lst2=[]
c_names={}
lst=inp.split(" ")
for name in lst:
    if c_names.get(name)==None:
        c_names[name]=1
    else:
        c_names[name]+=1
#print(c_names)
lst2=[v for v in c_names.values()]
maximum=lst2[0]
minimum=lst2[0]
for i in lst2:
    if i<minimum:
        minimum=i 
    elif i>maximum:
        maximum=i
#print(mini,maxi)
for k,value in c_names.items():
    if value ==maximum:
        print(k,":",value)
    elif value==minimum:
        print(k,":",value)
        
