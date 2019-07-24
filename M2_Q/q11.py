"""	Following are the initials of players who play various games. Some of these players play more than one game.
Cricket: [ "PKM", "ALN", "GLN", "NVR", "PVR", "KM", "VP", "CS", "MCS"]
Football: [ "PKM", "ALN","RMZ","CS", "MCS"]
Badminton: [ "PKM", "ALN", "NV", "KM","RMV"]

Write a program to:
a.	List those players who play all three games.
b.	List those players who play exactly one game."""


Cricket = [ "PKM", "ALN", "GLN", "NVR", "PVR", "KM", "VP", "CS", "MCS"]
Football = [ "PKM", "ALN","RMZ","CS", "MCS"]
Badminton = [ "PKM", "ALN", "NV", "KM","RMV"]
player=[]
player.extend(Cricket)
player.extend(Football)
player.extend(Badminton)
#print(player)
c_names={}
lst=[]
lst1=[]
lst2=[]
for name in player:
    if c_names.get(name)==None:
        c_names[name]=1
    else:
        c_names[name]+=1
lst=(c_names.values())

for k,value in c_names.items():
    if value ==3:
        lst1.append(k)
    elif value==1:
        lst2.append(k)

print("Players who play all three games:",lst1)
print("Players who play only three games:",lst2)






