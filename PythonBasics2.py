#How To Take Input From User

name=input("Enter your Name:")
print(name)

#TypeCasting
marks1=int(input("Enter your First Subj Marks"))
print(marks1)

marks2=int(input("Enter your Second Subj Marks"))
print(marks2)

print("Both Subjects Total Obtained Marks",marks1+marks2)

test=bool(input("0 for Male and 1 For Female"))
# This is just for the Boolean Values if we enter any input the boolvalue will be 1  or Ture and it will show Female if we not enter any input then the boolvalue will be 0 or False and it will compare accordingly and show Male as output.
int(test)
if test==0:
    print("Male")
elif test==1:
    print("Female")

#Lists Syntax in Python and We can change or update items in Lists
print("Lists Syntax in Python")
list1=["Hello", "Smith", "Roll No", 2, "Grade",'A']
list2=["John", "Jack", "Roll No", 9, "Grade",'B']
print(list1)
print(type(list1))
print(list2)
#UpDating Items in List
print("Updating Items in Tuple")
list1[0]="Bye"
list1[3]=3
print(list1)
list2[1]="Alex"
list2[5]="C"
print(list2)
#Tuple Syntax in Python and We cannot change or update items in Tuple
print("Tuple Syntax in Python")
tuple1=("New","Customer","Id",2)
print(tuple1)
print(type(tuple1))

#Dictionaries Syntax in Python

print("Dictionaries Syntax in Python")
dict1={"Name":"Alex","Class":"BSCS","Roll No":29,"Grade":'A'}
print(dict1)
print(type(dict1))

#Sets Syntax in Python

print("Sets Syntax in Python")
set1={"Salary","Month","Year"}
print(set1)
print(type(set1))

