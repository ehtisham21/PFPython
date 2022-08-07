def square(ls):
    square=[]
    for i in ls:
        square.append(i**2)
    return square
list1=[1,2,3,4,5]
res=square(list1)
print(res)

#Default Keyword in Functions
def addition(o=2,b=3): #If no argument is passed to the function from where it is called then the default value (o=2,b=3) will be used to perform action on the function
    add=o+b
    return add

a=9
q=addition(a)
print(q)


