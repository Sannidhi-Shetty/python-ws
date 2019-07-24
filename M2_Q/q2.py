"""2.	Write a program to accept a two-dimensional array containing integers as the parameter and determine the following from the elements of the array:
a.	element with minimum value in the entire array
b.	element with maximum value in the entire array
c.	the elements with minimum and maximum values in each column
d.	the elements with minimum and maximum values in each row"""
lst=[[0,1,2,3],[3 ,4,5, 5],[6 ,7, 8, 8],[9, 0, 1 ,9]]
print(f"minimum value of an element in an array:{min(map(lambda x:min(x),lst))}")
print(f"maximum value of an element in an array:{max(map(lambda x:max(x),lst))}")
min_col_val=list(min(map(lambda x:x[i],lst)) for i in range(4))
print(f"elements with minimum values column-wise: {min_col_val}")
max_col_val=list(max(map(lambda x:x[i],lst)) for i in range(4))
print(f"elements with minimum values column-wise: {max_col_val}")
min_row_val=list(map(lambda x:min(x),lst))
print(f"elements with minimum values row-wise:{min_row_val}")
max_row_val=list(map(lambda x:max(x),lst))
print(f"elements with minimum values row-wise:{max_row_val}")











