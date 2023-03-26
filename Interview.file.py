# import  operator
# import time
# # def student(name, age):
# #     print('Student Details:', name, age)
# #
# # # default function call
# # student('Jessa', 14)
# #
# # # both keyword arguments
# # student(age=12)
#
# def mulp(*args):
#     s = 1
#     for i in args:
#         s*=i
#     return s
# x = [1,2,3]
# y = [4,5,6]
# z=[2,2,2]
#
# t1 = time.time()
# a,b,c = map(mulp,x,y)
# print(a,b,c)
#
# t2 = time.time()
# print('total time taken for 1st val : %.9f'%(t2-t1))
#
# t1 = time.time()
# a,b,c = map(operator.mul,x,y)
# print(a,b,c)
#
# t2 = time.time()
# print('total time taken for 1st val : %.9f'%(t2-t1))

import itertools
print(list(itertools.product([3,4], repeat = 2)))