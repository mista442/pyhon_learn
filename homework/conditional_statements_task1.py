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
rand_bigger=0
rand_less=0

rand1 = random.randint(1,100)
print(rand1)
rand2 = random.randint(1,100)
print(rand2)
