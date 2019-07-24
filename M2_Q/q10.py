"""10.	Write a program to count the number of unique words and the number of occurrences of each of those words from the question provided below.
Input:
"How much wood would a woodchuck chuck if the woodchuck could chuck wood?"
Output:
Number of unique words: x
abcd: p times
efgh: q times
rstu: t times"""

data="How much wood would a woodchuck chuck if the woodchuck could chuck wood"
lst=[]
lst=data.split(" ")
#print(lst)
c_names={}
for name in lst:
    if c_names.get(name)==None:
        c_names[name]=1
    else:
        c_names[name]+=1
#print(c_names)
#lst1=(c_names.values())
count=0
for k,value in c_names.items():
    if value == 1:
        count+=1
    elif not value <2:
        print(k,":",value," times")

print("Number of unique words:",count)