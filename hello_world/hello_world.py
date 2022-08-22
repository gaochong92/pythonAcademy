'''
Author: gaochong
E-mail: gaochongs@163.com
Date: 2022-08-08 22:20:55
LastEditors: gaochong
LastEditTime: 2022-08-14 00:40:26
Description: hello world
FilePath: \python\hello_world\hello_world.py
'''
#变量
from audioop import add
import math


first_message = 'this is first message'

print(first_message)

first_message = 'this is second message'

print(first_message.lower())
a = abs

hex_data = 1024
print(hex(hex_data),type(hex(hex_data)))

print(a(-22))
#set
sets = set([1,2,3,4,'sds'])
print(sets)

# x = input('x的值是')


# #定义函数
# def my_abs(x):
#     x = int(x)
#     if x>0:
#         print(x)
#     else:
#         print(-x)

# my_abs(x)



# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny
# print(move(100, 100, 60, math.pi / 6))

# def varf(*num):
#     for x in num:
#         print(f'jianshi{x}canshushi')

# aa = [1,2,3,44,55,23,23]

# varf(*aa)

# def fact(n):
#     if n == 1:
#         return 1
#     return n*fact(n-1)

# print(fact(1000))

name = [n*n for n in range(1,10) if n % 2 == 0]
print(name)

g = (s**s for s in range(1,5))

for gg in g:
    print(gg)

