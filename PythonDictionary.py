dict1={"Name":"Joe","Section":"A","RegNo":3}
print(type(dict1))
print(dict1)

#Creating dictionary using built-in function dict()
dict2=dict({1:"PHP",2:"Python"})
print(dict2)

#Empty dictionary
dict3={}
print("Empty Dictionary", dict3)

#Creating a Dictionary with each item as a Pair
dict4=dict({(1,"Alo"),(2,"Joe"),(3,"Mic")})
print(type(dict4))
print(dict4)

#Accessing the dictionary values
dict5={"CGPA":2.09,"Class":"BSIT","RollNo":201}
print(dict5)
print("CGPA is :%f"%dict5["CGPA"])
print("Class is :",dict5["Class"])
print(dict5.get("RollNo"))

#Adding dictionary values
dict6={}
print("Empty Dictionary:",dict6)
dict6[0]="Alex"
dict6[2]=1
dict6["Result"]="CGPA"
print("After Adding Values To Dictionary",dict6)

dict6["University Class"]=22,4,6
print(dict6)
dict6["Result"]="Pass"
print("After Updating Value of Result",dict6)

#Update Dictionary values from taking user input
dict7={"Name":"Alex","Class":"BS","RollNo":901}
print("Before Updating Values",dict7)
dict7["Name"]=input("Update Name Value")
dict7["Class"]=input("Update Class Value")
dict7["RollNo"]=input("Update RollNo Value")
print("After Updating Values",dict7)

#Deleting elements using del keyword
del dict7["Class"]
print(dict7)

#Deleting an element using pop() method
dict7.pop("RollNo")
print(dict7)


#Deleting the whole dict9 dictionary
''''dict9={1:2,2:3,4:5}
print(dict9)
print("Deleting the whole dict9 dictionary")
del dict9
print(dict9)'''''

#For loop to print all the keys of a dictionary
print("To print all the keys of a dictionary")
Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}
for x in Employee:
    print(x)

#For loop to print the values of the dictionary
print("To print all the values of a dictionary")
students={"Marks":22,"Id":3,"Result":"Pass"}
for y in students:
    print(students[y])

print("To print all the values of a dictionary using values() method")
for y in students.values():
    print(y)

#For loop to print the items of the dictionary by using items() method
print("To print all the items of a dictionary using items() method")
for y in students.items():
    print(y)

'''
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which changeable. No duplicate keys but values can be duplicate or same.

'''