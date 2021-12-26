"""
1. In build function: print(),len(),dir(),type()
2. User Define function
"""

# function define
# def test():
#     # function body part
#     print("Hello function")
#
#
# # calling function
# test()


# def add(x, y):
#     print(x + y)
#
#
# add(10, 20)
# * args
# ** kargs

#
# def user(*names, **data):
#     print(names)
#     print(data)
#
#
# user('ram', 'sita', 'hair', name='sophia', phone=303456543)
#
#
# def total(*numers):
#     print(numers)
#
#
# user(12, 234, 45)


# def users(name):
#     print(f"hello function {name}")
#
#
# users('user define')

# x = 20
#
#
# def test():
#     global x
#     x = x + 10
#     print(x)
#
#
# test()
# print(x)

#
# def test():
#     pass
#
# print(test())

# def add_sub(x, y):
#     tot = x + y
#     s_tot = x - y
#     return [tot, s_tot]
#
#
# res = add_sub(20, 10)
# print(res)

# def student():
#     def name(new_name):
#         return new_name
#
#     return name
#
#
# x = student()
# print(x('hari'))


# ptr = lambda p, t, r: p * t * r / 100
# print(ptr(10, 10, 10))


# def insert():
#     """
#     Insert function use for data insert into table
#     """
#     return 'Done!'
#
# # print(insert.__doc__)
# # print(print.__doc__)
# print(insert.__name__)

# def test():
#     return "Hello"
#
#
# def user():
#    print(test())
#
#
# user()

#
# def take_value():
#     pass
#
# def calculate():
#     pass
#
# def display():
#     pass

# if __name__ == "__main__":
#     pass

# print(__name__)


# def add(x, y):
#     return x + y
#
#
# if __name__ == '__main__':
#     print(10, 10)

# def my_function(any_function):
#     def inner_function():
#         print(any_function.__doc__)
#
#     return inner_function
#
#
# @my_function
# def add():
#     """hello add function"""
#     return "hello"
#
#
# add()

# def zero_check(any_fun):
#     def inner_function(x, y):
#         if y == 0:
#             return "Y is zero"
#
#         else:
#             return x + y
#
#     return inner_function
#
#
# @zero_check
# def add(x, y):
#     return x + y
#
#
# print(add(20, 10))

#
# import calculator
#
# print(calculator.add(20, 20))
#
# from calculator import add,sub,mul
#
# print(add(20, 30))
#
# import sys
# import os


# from lib import *
# #
# print(demo.test())
# print(users.add())


# def test():
#     print("Hello function")
#
#
# test()

#
# def add(x, y):
#     print(x + y)
#
#
# add(10, 20)

# def users(name):
#     pass
#
#
# print(users('ram'))


# import calculator
# from calculator import add
#
# print(add(10, 20))
# print(add(30, 20))

# print(calculator.add(20, 20))
# print(calculator.sub(20, 10))
#
# from lib import *
#
# print(song.play())

# import os
# import sys
# import  glob

# import os
# print(dir(os))

# print(os.getcwd())
