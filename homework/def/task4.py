"""Задача 4 Дан список целых чисел. Посчитать, сколько раз в нем встречается каждое
число. Например, если дан список [1, 1, 3, 2, 1, 3, 4], то в нем число 1 встречается три раза,
число 3 - два раза, числа 2 и 4 - по одному разу."""

# код без функции

# l = [1, 1, 3, 2, 1, 3, 4]
# l.sort()
# print(l)
# l1 = [] # создаем уникальный лист куда будем складывать только уникальный элементы
# for i in l:
#     if i not in l1:
#         l1.append(i)
# print(l1)
#
# for i in l1:
#     print("число",i,"встречается",l.count(i),"раз")

# код с функциями

import random
def GenLists():

        l=[]
        n=int(input("укажите количество элементов в списке: "))

        for i in range(n):
                a=random.randint(1,4)
                l.append(a)
        l.sort() # сортируем полученный список
        return l

list = GenLists()
print(list) # отображаем полученный сгенериррованный список

def Get_uniq_items():
    l_uniq = []
    for i in list:
        if i not in l_uniq:
            l_uniq.append(i)
    return l_uniq
list_uniq = Get_uniq_items()
#print(list_uniq)

def Print_count_uniq_items():
    for i in list_uniq:
        print("число",i,"встречается",list.count(i),"раз")
Print_count_uniq_items()
