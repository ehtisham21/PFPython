tup1=("Jass","Joe",2)
print(tup1)
print(type(tup1))
print(tup1[0:2])

#Creating a tuple with single element
yy=("Alex")
print(type(yy))

zz=("Jass",)
print(type(zz))

tup2=("Smith","John","Jack","Alex")
for u in tup2:
    print(u)

#Taking input from user Directly in Tuple
tup3=tuple(input("Enter values in Tuple"))
for o in tup3:
    print("You Entered",o,"in Tuple")
print(tup3)
print("The value at index 2: ",tup3[2])

tup4=(1,2,5,7,9)
print(tup4*2)
print("The length is ",len(tup4))
print(tup4+tup3)

a=2 in tup4
print(a)

print("The maximum element in tuple is ",max(tup4))
print("The minimum element in tuple is ",min(tup4))
