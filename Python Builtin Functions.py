#Python abs() Function The python abs() function is used to return the absolute value of a number. It takes only one argument, a number whose absolute value is to be returned.
a=-99
print(abs(a))
print(abs(-7))

#Python all() Function The python all() function accepts an iterable object (such as list, dictionary, etc.). It returns true if all items in passed iterable are true. Otherwise, it returns False. If the iterable object is empty, the all() function returns True.
list1=[1,0,True] #One False Value which is 0
tup1=(True,) # One True Value
print(all(list1))
print(all(tup1))
list2=["Alex",False] #One Value is False
print(all(list2))

#Python bin() Function The python bin() function is used to return the binary representation of a specified integer. A result always starts with the prefix 0b.
x=10
print(bin(x))


#Python bool() The python bool() converts a value to boolean(True or False) using the standard truth testing procedure. If no parameter is passed, then by default it returns False. So, passing a parameter is optional.
a=False
print(bool(a))
b="Hello"
print(bool(b))
c=None
print(bool(c))
d=[1,0,2]
print(bool(d))
e=[]
print(bool(e))


#Python sum() Function As the name says, python sum() function is used to get the sum of numbers of an iterable, i.e., list.
sum1=(1,4,3,2,4,5)
print(sum(sum1))
sum2=[22,4,21,3,4,6,21]
print(sum(sum2))


#Python any() Function The python any() function returns true if any item in an iterable is true. Otherwise, it returns False.
i={1,2,3,4,5}
print(any(i))
o=[False]
print(any(o))
l = []
print(any(l))


#Python float() The python float() function returns a floating-point number from a number or string.
d=2
print(float(d))
print(float(12))
print(float(-6.2))

#Python iter() Function The python iter() function is used to return an iterator object. It creates an object which can be iterated one element at a time.
lis=[1,2,3,4,5,6,7]
lisiIter=iter(lis)
print(next(lisiIter))
print(next(lisiIter))
print(next(lisiIter))
print(next(lisiIter))
print(next(lisiIter))
print(next(lisiIter))
print(next(lisiIter))


#Python enumerate() Function
listt=[1,2,4,3,5,6,7,43,24,5]
result = enumerate(listt,3)  #In this the listt argument is (Iterable: any object that supports iteration) and the argument 3 is (Start: the index value from which the counter is to be started, by default it is 0)
print(result)
print(list(result))

stocks = ["alez", 'system', 'tcs']
prices = [9, 2, 7]
qq = [1, 3, 2]
resultt=zip(stocks,prices,qq)
print(set(resultt))