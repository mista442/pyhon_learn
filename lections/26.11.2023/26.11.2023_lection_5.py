#10 декабря не занимаемся

# Функции

# подпрограмма 1 - ввод информации
# подпрограмма 2 - анализ информации
# подпрограмма 3 - вывод результата анализа информации

# функцию надо сначала реализовать, а только потом ее использовать

''' способы передачи результата обработки данных:
- глобальные переменные (глобальные переменные плохи тем, что к ним могут обратиться другие функции, использующие теже имена переменных)

'''
import random


# глобальные переменные

# a=0 # global
# b=0 # global
# def InputData(): # создание функции и описание команд, что в нее входит
#     # локальные перменные
#     global a,b # переделываем локальные переменные в глобальные. Теперь основная программа про них будет знать.
#     a = int(input("введите первое число ")) # local
#     b = int(input("введите первое число ")) # local
#
# InputData() # вызов функции - на этом этапе будут выполняться вложенные в функцию команды
#
# sum = a + b # переменная sum ничего не значен про команды внутри функции. Ей нужно как-то передать данные в переменную
# print("сумма двух чисел ",sum)

# nonlocal - перезаписывает переменную ну уровень выше

# a = 50
# def f1():
#     x = 100
#     def f2():
#         nonlocal x
#         x = 200
#     f2()
#     print(x)
# f1()
# print(x)

#---------------------------

# a = 50
# def f1():
#     x = 100
#     def f2():
#         global x
#         x = 200
#     f2()
#     print(x)
# f1() # 100
# print(x) # 200

#----------------------

# def InputData(): # создание функции и описание команд, что в нее входит
#     # локальные перменные
#     a = int(input("введите первое число ")) # local
#     b = int(input("введите первое число ")) # local
#     return a,b # возвращает основной программе результат (чтобы не использовать глобальные переменные)
#
# def Summa(n1,n2):
#     s=n1+n2
#     return s
#
# x,y = InputData() # в x - запишется результат переменной a, в y - запишется результат переменной b
#
# sum=Summa(x,y) # Read Only
# print(sum)
#
# def Print(number):
#     print("сумма двух чисел равна ", number)
#
# Print(sum)
import  random
def InputData(): # создание функции и описание команд, что в нее входит
    a = int(input("введите количество чисел "))
    list = []
    for i in range(a):
        list.append(random.randint(-100,100))
    return list

def FindMax(www):
    www.sort()
    www[-1]=999 # Read and Write
    return www[-1]


qqq = InputData()
print(qqq)

max=FindMax(qqq) # передача данных по ссылке. Если хотим передать по значению, то через срез/.copy
print(max)

# max=FindMax(qqq[:]) - через срез
# max=FindMax(qqq.copy) - через .copy

print(qqq)

def test(function):
    return function(5)

def add_one(x):
    return  x + 1

print(test(add_one))
