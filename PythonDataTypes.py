a=5
b="Alex"
c=0.9

print(type(a))
print(type(b))
print(type(c))

#Numbers

p=9
print("It is a int number",isinstance(p,int))

i=2.39
print("It is a float number",isinstance(i,float))

#String
str1="My name is"+"Alex"
print(str1)

str2=""" My name is
John 
and I am 
learning python
"""
print(str2)

str3="Hello Alex"
str4='How are you'

print(str3[0:7])  #printing first seven character using slice operator
print(str4[5])    #printing 5th character of the string
print(str3*4)     #printing the string four times
print(str3+str4)  #printing the concatenation of str3 and str4

#List

list1=["Name","Tom","GPA","2.8"]
print(list1)
print(type(list1))

list2=["ID",1]
print(list2)

print(list1[0:2])
print(list1[-1]) # -1 indicated the last element in the list
print(list2[0:])

print(list1[0:]+list2[0:])

#Update List Items
list1[2]="CGPA"
print(list1)

list2[1]=2
print(list2)

#List Methods
#index Method
print(list1.index("Tom"))

#count Method
print(list2.index("ID"))

#Sort Method:
listy=[0,10,4,6,8,4,1,2]
listy.sort()
print(listy)
listy.append(11)
print(listy)
oo=list(["A",4])
print(oo)
print(type(oo))
#Sort List in Descending Order
listy.sort(reverse=True)
print(listy)

#Remove Method
listy.remove(11);
print(listy)

#Pop Method
listy.pop(0)  #removed the 0 index value that is 10 in this case
print(listy)
listy.pop()   #removed the last index value that is 0 in this case
print(listy)

#Extend Method
listy.extend([10,11,12,13])
print(listy)

#Insert Method
listy.insert(0,[9,10,11])
print(listy)


#Tuple
tup1=("Hello","Smith",0)
print(tup1[0:1])
print(tup1[1:])

w=tuple(["ht","Ahi",0])
print(w)