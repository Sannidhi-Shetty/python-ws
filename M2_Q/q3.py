"""3.	Write a program to determine the work hours of the day entered based on the timetable provided below."""
d={'Mon':[3,2,2],'Tue':[3,2,2],'Wed':[3,2,2],'Thu':[3,2,1],'Fri':[3,2,1],'Sat':[3,1,0],'Sun':[0,0,0]}
inp=input("Input:")
for a,b in d.items():
    if inp==a:
        print(f"{b}")