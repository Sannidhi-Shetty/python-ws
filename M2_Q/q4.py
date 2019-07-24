"""Write a program to accept an input string from the user and determine the vowels in the string and calculate the number of vowels"""
name=input("Enter ur name:")
lst=['a','e','i','o','u']
lst1=list(filter(lambda x:x in lst,name))
print(lst1,len(lst1))
print()