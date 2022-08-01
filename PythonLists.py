a = [1,2,"Peter",4.50,"Ricky",5,6]
b = [1,2,5,"Peter",4.50,"Ricky",6]
print(a ==b)

c = [1, 2,"Peter", 4.50,"Ricky",5, 6]
d = [1, 2,"Peter", 4.50,"Ricky",5, 6]
print(c ==d)

list1=["John","BSCS",25]
print("%s study in %s and he is %d years old"%(list1[0],list1[1],list1[2]))

#Print SubList from a List
list2=[1,2,3,4,5,6,7,8,9,10]
print(list2[1:9])
print(list2[0:10:2])

list3=[2,3,4,5,7,5,3,4]
print("List 3")
print(list3[-8:-1])
print(list3[-7:-3])

#Updating The List Values
lis4=[2,5,4,5,7,25,33]
print("List 4")
print(lis4)
lis4[6]=34
print(lis4)
lis4[0:3]=[1,2,3]
print(lis4)
print("Deleting Elements from List")
del lis4[0:2]
print(lis4)

list5=[]
p=int(input("How many numbers you want to add in the List"))
for i in range(0,p):
    list5.append(input("Enter Number"))

print("Numbers Entered in the List")
for j in list5:
    print(j)

up=input("Enter the Number which you want to Delete from the list")

for k in list5:
    if k==up:
     list5.remove(up)
print("The Deleted Number is",up)
print(list5)