'''Задача 6. Даны два списка целых чисел одинаковый длины. Например [5,4,3] и [2,1,3].
Сформировать третий список полученный путем нахождения разницы меду списками,
например [5-2, 4-1,3-3] итоговый список [3,3,0].
Формирование третьего списка осуществляется с использованием функции'''


import random

def GenLists():

        l1=[]
        l2=[]

        n=int(input("укажите количество чисел: "))

        for i in range(n):
                a=random.randint(1,10)
                b=random.randint(1,10)
                l1.append(a)
                l2.append(b)
        return l1,l2

list1,list2 = GenLists()
print(list1)
print(list2)

def Raznost():
        l3=[]
        count = 0
        for i in list1:
                l3.append(list1[count]-list2[count])
                count = count + 1
        return l3
list3 = Raznost()
print("Разность элементов между 1 и 2 списком\n", Raznost())
