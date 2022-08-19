from numpy import *
#1D Array using Numpy
studata=array([1,2,3,4,15,6,7],int)
so=array([1,2,6,8,10,12,7],int)
for i in range(len(studata)):
    print(studata[i])

# Mathematical Operaitons on Arrays using numpy
st=studata+5
print(st)

sut=studata-5
print(sut)

#Comparing Arrays but make sure that size of both arrays must be smae
x=studata==so
print(x)

#Where() Funciton is used to create a new array which contains returned element chosed from expression 1 or expression 2 depending on condition. If condition is True expression 1 will be executes otherwise expression2.

c=where(studata>so,studata,so)
print(c)

# Copy() Method is used to create a copy of an existing array. If the new array get modified, the existing array will not be affected or vise vera. Both arrays are independent.
stp=array([1,3,5,7,9,11],int)
sou=stp.copy()
print(stp, id(stp))
print(sou, id(sou))

print("After Changing the array elements")
stp[2]=6
print(stp)
print(sou)

s=int(input("How many elements you want to enter"))
sus=zeros([s],int)
for o in range(len(sus)):
    u=int(input("Enter Number"))
    sus[o]=u
print(sus)


#2D Array
a=array([ [11,12,13,14,15],[16,17,18,19,20]])
for pp in range(len(a)):
    for u in range(len(a[pp]):
        print(o)