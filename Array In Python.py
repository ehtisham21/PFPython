# import array
# studentdata=array.array('i',[100,101,102,103,104,105])

# OR

from array import *
studentdata=array('i',[100,101,102,103,104,105])
print(studentdata[0])

studat=array('f',[1.1,1.2,1.3])
n=len(studat)
for i in range(n):
    print(studat[i])
j=0
while j<n:
    print(studat[j])
    j+=1

#Add Element at the end of the array index
studat.append(2.88)
print(studat)

#Take Input from User Using For Loop and Add it To Array
st=array('i',[])
u=int(input("How many Elemnts you want to Add in the Array"))
for o in range(u):
    st.append(int(input("Enter Number")))
for r in range(len(st)):
    print(st[r])

# Take Input from User Using While Loop and Add it To Array
swt=array('i',[])
ou=int(input("How many Elemnts you want to Add in the Array"))
pp=0
while pp<ou:
    swt.append(int(input("Enter Number")))
    pp+=1
r=len(swt)
op=0
while op<r:
    print(swt[op])
    op+=1

# Insert Method is used to insert an element in a particular position.
swt.insert(3,20)
print(swt)

# POP Method is used to remove last element.

swt.pop()
print(swt)

#POP(n) is used to remove an element by position number from a particular position and return removed element.
o=swt.pop(2)
print(swt,"The removed element is",o)


# Remove Method is used to remove first occurence (like if array have 2 elements of 101 it will remove the first 101 element) of given element and if it doesnot found the element, shows value error.
swt.remove(101)
print(swt)

# Reverse Method is used to reverse the order of elements in the array. For example [1,2,3,4,5] it will reverse to[5,4,3,2,1]
swt.reverse()
print(swt)

# Extend Method is used to append another array or iterable object at the end of the array.
arr1=array('i',[1,3,5,7,9])
arr2=array('i',[2,4,6,8,10])
arr1.extend(arr2)
print(arr1)

#Slicing on Array can be used to retrieve a piece of the array that contains a group of elements. Slicing is useful to retrieve a range of elements.
arr3=array('i',[1,2,3,4,5,6,7,8,9])
a=arr3[2:5]
for sd in a:
    print(sd)
print("Slicing using For Loop")
for oo in arr3[0:3]:
    print(oo)