'''1. Напишите программу, которая запрашивает у пользователя три числа в диапазоне
1-1000. Компьютер генерирует два случайных числа в диапазоне 1-100, которые
определяют отрезок. Определить какие числа указанные пользователям попали в
отрезок.'''


flag=True
while flag:
    print("введите 3 числа в диапазоне от 1 до 1000")
    a=int(input())
    b=int(input())
    c=int(input())

    if a < 1 or a > 1000 or b < 1 or b > 1000 or c < 1 or c > 1000:
        print("вы ввели числа вне заданного диапазона, повторите попытку")
    else:
        flag=False

import random
rand1 = random.randint(1,100)
rand2 = random.randint(1,100)

l=[]
l.append(rand1)
l.append(rand2)
l.sort()

flag1=True
while flag1:
    if a > l[0] and a < l[1]:
        print(a,"находится в заданном диапазоне")
    else:
        flag1=False
    if b > l[0] and b < l[1]:
        print(b,"находится в заданном диапазоне")
    else:
        flag1=False
    if c > l[0] and c < l[1]:
        print(c,"находится в заданном диапазоне")
    else:
        flag1=False
    if (a < l[0] or a > l[1]) and (b < l[0] or b > l[1]) and (c < l[0] or c > l[1]):
        print("ни одно из чисел пользователя не попало в отрезок")
    else:
        flag1=False