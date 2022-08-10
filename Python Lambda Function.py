num=lambda a:a+2
print(num(8))

def reciprocal(x):
    return 1/x
print(reciprocal(20))

recep=lambda y:1/y
print(recep(20))


o=[11,2,44,6,3,123,4,6,67,54,6,1,2,42,8]
print(list(filter(lambda even: (even%2==0),o)))

numbers_list = [2, 4, 5, 1, 3, 7, 8, 9, 10]
print(list(map(lambda num: num ** 2, numbers_list)))


min=lambda x,y:x if(x<y) else y
print(min(2,3))