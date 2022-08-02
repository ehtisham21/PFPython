set1={1,2,3,"Python","Java"}
print(set1)
print(type(set1))

#Second Way to create Set using Set()
days=set(["Monday",1,"Tuesday"])
print(days)

for i in days:
    print(i)

#Creating Empty Set
set2={}
print(type(set2))  #Creating an empty set is a bit different because empty curly {} braces are also used to create a dictionary as well. The Type outout for this is Dictionary

set3=set()
print(type(set3)) #The empty set can be created with set() function

#Adding Duplicate elements to set and the set will remove the duplicate items.
set4={"Alex","James",2,"Alex",2}
print(set4)

#Adding items to the set using add() and update() function
set5={1,2,3,4,5,6,7,"Monday"}
print(set5)
print("After adding elements to the set using add() function")
set5.add("Tuesday")
print(set5)
print("After adding elements to the set using add() function")
set5.update(["Wednesday",8,"Thursday"])
print(set5)

#Removing items from the set using discard() and remove() function
set5.discard(2)
set5.discard("Thursday")
print(set5)
set5.remove(8)
print(set5)
set5.remove("Monday")
print(set5)
#We can also use the pop() method to remove the item. Generally, the pop() method will always remove the last item but the set is unordered, we can't determine which element will be popped from set
print("Removing using POP Function")
set5.pop()
print(set5)

#Clear() method to remove all the items from the set.
print("Removing all items from set using clear function")
set5.clear()
print(set5)

#Union of two Sets using || and union() function
month1={"Jan","Feb","March"}
month2={"April","May","June"}
print(month1|month2)
print(month1.union(month2))

#Intersection of two sets using and & operator or the intersection() function
days1={"Friday","Saturday","Wednesday"}
days2={"Monday","Friday","Wednesday"}
print(days1&days2)
print(days1.intersection(days2))

#intersection_update() method is used to remove the items from the original set that are not present in both the sets (all the sets if more than one sets are specified).
print("Intersection_update() method")
name1={"Alex","Jordan","Smith","Ham"}
name2={"Joe","Jassy","Susan","Jordan","Ham"}
name3={"Michael","Ham"}
name1.intersection_update(name2)
name3.intersection_update(name1,name2)
print(name1)
print(name3)

