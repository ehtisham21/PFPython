def square(ls):
    square=[]
    for i in ls:
        square.append(i**2)
    return square
list1=[1,2,3,4,5]
res=square(list1)
print(res)

#Default Arguments in Functions
def addition(o=2,b=3): #If no argument is passed to the function from where it is called then the default value (o=2,b=3) will be used to perform action on the function
    print("Default Arguments")
    add=o+b
    return add

a=9
q=addition(a)
print(q)


#Keyword Arguments in Functions
print("Keyword Arguments")
def subtract(a,b):
    sub=a-b
    return sub
f=subtract(11,10) #In this function call 11 and 10 are positional arguments.Positional arguments are values that are passed into a function based on the order in which the parameters were listed during the function definition. Here, the order is especially important as values passed into these functions are assigned to corresponding parameters based on their position.
e=subtract(10,b=12) #But we must keep in mind that keyword arguments must follow positional arguments. Having a positional argument after keyword arguments will result in errors.Keyword arguments come after positional arguments and before default/optional arguments in a function call.In this function call a is positional argument and b is the keyword argument and b follows a.
print(e,f)

#Arbitrary Arguments
print("Arbitrary Arguments")
def team(*members): #*args: for non-keyworded/positional arguments and **kwargs: for keyworded arguments. A single asterisk signifies elements of a tuple, whereas double asterisks signify elements of a dictionary.
    for i in members:
        print(i)
team("Abena", "Marilyn","Alex","Sim",1,2,3)

def team(**memb):
    for ky,vues in memb.items():
       print(ky,":",vues)
team(Name= "Mic",Project="Final Year",Class="BSCS")

#Lambda or Anonymous Functions
lamb=lambda num1,num2:num1*num2
print(lamb(2,5))