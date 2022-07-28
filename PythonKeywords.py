import keyword
print("The keywords are ",keyword.kwlist)
#OR
print(help("keywords"))

#Value Keywords: True, False, None

a=8
b=9
if a==b:
    print(True or False)
else:
     print(True and False)

print(True + False + False)     #1+0+0
print(False+False+False)        #0+0+0

if True==1:        #Can Change Value 1 To 5 to check if it is giving the False Bool Value Correct or Not
    print("True Value is Correct")
elif False==0:
    print("False Value is Correct")

else:
    print("Please Enter Value in Between 0 and 1")

#None Keyword
print(None==0)
print(None==None)

#Operator Keywords: and, or, not, in, is

#OR
print("OR Keyword")
print(True or False)
print(False or False)

#And
print("And Keyword")
print(True and True)
print(False and True)

#Not
print("Not Keyword")
print(not True)
print(not False)

#In Keyword
print("In Keyword")
smi="Smith Joe"
print("Smith" in smi)
print("th" in smi)
print("y " in smi)

#Is Keyword
print("Is Keyword")
print(True is False)
print(True is True)
print(True is not False)
print(2+2 is 3)