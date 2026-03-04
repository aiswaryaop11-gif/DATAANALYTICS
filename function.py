
# function #--------------------------------------

# c program
# function function_name(){
#     code
# }
# function_name()


# in python#

# def function_name():
#     Code
# def func1():
#     print('haiii')
# func1()
# func1()
# func1()



# def fun2(a,b):           # parameters--------------------------1
#      print(a,b)
# fun2(5,5)            # arguments-----------------------------2


# sum of two number-----------------------------------

# def func2(a,b):
#     print(a+b)
# func2(4,6)


# arbitrary arguments--------------------------------------------3

# def name(*name):
#     print(name)
# name('ammu','anu','anu')


# positional arguments-----------------------------------------4

# def fun3(name,place):
#     print(name)
#     print(place)
# fun3('anu','kozhikode')


# keyword arguments------------------------------------------5

# def func3(name,place):
#     print(name)
#     print(place)
# func3(place='kannur',name='ammu')



# arbitrary keyword arguments---------------------------------------6

# def func4(name,email,place):
#     print(name)
#     print(email)
#     print(place)
# func4(name='ammu',email='ammu@gmail.com',place='kozhikode')

# def func4(**data):
#     print(data)
# func4(name='ammu',email='ammu@gmail.com',place='kozhikode')



# default parameters---------------------------------------------------------------7

# def func5(name,place='kozhikode'):
#     print(name)
#     print(place)
# func5('ammu','kannur')
# func5('ammu')


# using pass keyword #

# if True:
#     pass
# def func7():
#     pass
# print('hello')


# positional argument only----------------

# def fun8(a,/):
#     print(a)
# fun8('ammu')

# keyword only aqrgument------------------

# def fun9(*,a):
#     print('ammu')
# fun9(a='anu')


# positional and -----------------

# def fun11(x,y):
#     print(x)
#     print(y)
# fun11('ammu',y='anju')
# fun11(y='anju','ammu')


# def fun10(x,y,/,w,z):
#     print(x)
#     print(y)
#     print(w)
#     print(z)
# fun10('x','y',w='w',z='z')


# global------------

# def fun12():
#     global a
#     a=5+5
    # print(a)
# fun12()
# print(a)


# recation--------------------#

# def fun12():
#     a=5+5
#     return a
# x=fun12()
# print(x)


# recation

# def sum(n):
#     if n<1:
#         return n
#     else:
#         return n +sum(n-1)
# print(sum(5))


# import math-----------
# import math
# x=math.sqrt(64)
# x=math.pow(4,3)
# print(x)


# import datetime--------------

# import datetime
# x=datetime.datetime.now()
# print(x.date())
# print(x.year)
# print(x)


# from func1 import func6
# func6()


# a=int(input('enter a num1:'))
# b=int(input('enter a num2:'))
# z=input('enter operation :')
# def fun1(a,b):
#     if z=="+":
#         print(a+b)
#     elif z=="-":
#         print(a-b)
#     elif z=="*":
#         print(a*b)
#     elif z=="/":
#         print(a/b)
# fun1(a,b)


# import random
#  print(random.randrange(1,11,2))
# print(random.randint(1,9))
# l=['ammu','anu','anju','rohan']
# s='python'
# print(random.choice(l))
# print(random.choice(s))


# gussing game--------------------------------------------#

# import random
# a=random.randint(1,9)
# for i in range(0,3):
#     guss=int(input('guss the number 1 to 9 :'))
#     b=(a-1),(a+1)
#     if guss==i:
#         print('you are winner')
#     elif guss==i:
#         print('you are winner')
#     elif guss==i:
#         print('you are winner')
#     else:
#         print('you are not winner')


# Lambda function----------------------------------------------------#

# def func1(x):
#     return x+5
# y=func1(5)
# print(y)


# x=lambda x:x+5
# z=lambda x,y:x+5
# print(x(5))
# print(z(5,5))


# simple description------docstring using---------------#

# def func():
#     '''this is simple description'''
#     """this is simple description"""
#     return None
# print(func())
# print(func.__doc__)


# even or odd ---function used-----------------------#

# x=lambda n:'even' if n%2==0 else 'odd'
# print(x(2))
# print(x(5))


#  mark--------------------#

# mark=[('anu',45),('ammu',23),('anju',30)]
# mark.sort(key=lambda x:x[1])
# print(mark)


# using reverse--------------#

# mark=[('anu',45),('ammu',23),('anju',30)]
# mark.sort(key=lambda x:x[1],reverse=True)
# print(mark)


# lambda function------#

# filter----------------------------1
# x=[1,2,3,4,5,6,7,8,9]
# y=tuple(filter(lambda a:a % 2==0,x))
# print(y)

# map-------------------------------2

# x=[1,2,3,4,5,6,7,8,9]
# y=list(map(lambda a :a*2,x))
# print(y)

# Reduce method------------------------3

# from functools import reduce
# x=[1,2,3,4,5,6,7,8,9]
# sum=reduce((lambda a,b:a+b),x)
# print(sum)









        

















