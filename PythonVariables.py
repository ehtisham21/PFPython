name="Joe"
Class="BSCS"
Subject="Python"

print("Name:",name,"Class:",Class,"Subject:",Subject)

print(id(name))
print(id(Class))
print(id(Subject))

#Multiple Assignment

x=y=z="Alex"
print(x,y,z)

a,b,c="Tom","John","Smart"
print(a,b,c)

#Deleting a Vairable
"""del a,b,c
print(a,b,c)"""


#Unpacking a list into a variable

listp=["Apple","Juice","Orange"]
f=listp
print(f)

listq=["Name","GPA","CGPA"]
u,i,h=listq
print(u,i,h)