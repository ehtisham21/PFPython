import random

a="Alex Justin"
for b in a:
    print(b)
    if b =="u":
        print("If")
    else:
      print("Else")
else:
    print("Loop Ended")

#Range in Python
t=range(10)
print(t)
print(tuple(t))

print(range(0,7))
print(list(range(0,7)))
print(list(range(2,10,2)))           #(Start 2,Stop 10,Step Size 2)

listy=("Alex","Joe","Smith")
for o in listy:
    print(len(o))

listu=[2,4,55,24,77,8,1,2,0]
sum=0
for val in listu:
    sum+=val**2
print(sum)

numbers=[1,3,4,35,45,3,5,22]
for num in range(len(numbers)):
    print(num)

alex=[]
for t in range(1,10):
    alex.append(random.randint(1,10))
print(alex)
for nu in range(1,10):
    for i in alex:
        if nu==i:
            print(nu, "Number Found")