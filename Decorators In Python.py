def dec(fu):
    def newfunction():
        print("I am not added to the Test Function now")
        fu()
        print("Now I am added to the Test Function")
    return newfunction

def test():
    print("Waiting For Decorator to Enhance the functionality without modifying the actual function")
tt=dec(test)
tt()


#Write a program to return 15 wihout modifying the number() function only 10 will return from number() function.
def modi(no):
    def nunew():
       print("15 Not Added to Number Function")
       a=no()
       b=a+5
       return b
       print("15 Added To Number Funciton",b)
    return nunew

def number():
    return 10
np=modi(number)
print(np())


