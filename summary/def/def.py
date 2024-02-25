# 2.9 лекция - функкции. 26.11.2023

#  ______               ____________
# |      | ----------> |            |
# |      |             | Function 1 |
# |      | <---------- |            |
# |      | send result --------------
# | MAIN |
# |      |              ____________
# |      | -------->   |            |
# |      |             | Function 2 |
# |      | <--------   |            |
# |      | send result  -------------
# |      |
# |      | send agrs
# |      | (optional)    ___________
# |      | ----------> |            |
# |      |             | Function 3 |
# |      | <---------- |            |
# |______| send result  ------------

'''MAIN - это основная программа, которая вызывает функции 1,2,3 во время выполнения.
Функции помогают сократить количество кода. Чтобы не писать один и тот же код множество раз,
а вызвать функцию в которой уже написан нужный код, и потом только вызывать эту функцию в нужных местах программы.
Функции можно в дальнейшем использовать и в других программах (в других main'ах)

Для передачи функции другим программистам - функцию можно опубликовать в модуль, чтобы ей могли пользоваться другие программисты в своих программах.
'''

# синтаксис функции:

# def <имя функции>(<args>):
#       <body def>
# <имя функции>() - вызов функции

# args - это параметры, которые передает основная программа функции в качестве аргументов (опционально)
# body def - код, который будет выполняться внутри тела функции
# <имя функции>() - вызов функции для выполнения и передачи результата основной программе

# Основная программа ничего не знает про то что происходит внутри тела функции.
# Поэтому основная программа может только вызвать функцию и получить от нее результат и дальше его как-то обрабатывать.
# есть еще варианты как вернуть данные из функции для основной программы, но про это чуть ниже

# Когда функция создана, она ещё ничего не выполняет. Только при
# вызове функции действия, которые в ней перечислены, будут
# выполняться.

# в основной прогрмамме нельзя сначала вызвать функцию, а только потом ее обьявить.
# но это будет работать, когда в рамках одной функции описываем другую:

### так нельзя - в основной программе вызвать функцию, а только пото ее обьявить --------------

# number = int(input("Введите целое число: "))
# if number >= 0:
#     positive()
# elif number < 0:
#     negative()
#
# def positive():
#     print("Положительное")
#
# def negative():
#     print("Отрицательное")
#
# ### так можно - внутри функции вызвать функцию, а только потом  ее обьявить -----------
#
# def test():
#     a=int(input("введите целое число "))
#     if a >= 0:
#         positive()
#     else:
#         negative()
# def positive():
#     print("положительное")
# def negative():
#     print("отрицательное")
# test()

#-------------------------

# в данном примере функция не вызывается, поэтому выполнена не будет

# def test():
#     print('hello')

# этом примере она вызывается - test()

# test() # после вызова функции test - будет выполнено тело функции - print('hello')

#-------------------------

# программа подсчета суммы 2 чисел

# a = int(input("введите первое число "))
# b = int(input("введите второе число "))
#
# summa = a + b
#
# print("сумма двух чисел =", summa)

# реализуем данную программу в виде нескольких функций

# func1 - ввод информации
# func2 - анализ информации
# func3 - вывод результата анализа информации

# func1
# def InputData():
#     a = int(input("введите первое число "))
#     b = int(input("введите второе число "))
#
# # вызываем функцию InputData
# InputData()
#
# def SumData():

#--------------------------------------------------
# cпособы как подпрограмма передавать данные из тела функции для основной программы:

# - использование глобальных переменных
# - использование return
# - использование файлов
# - передача аргументов по ссылке

# ---

# Глобальные переменные - те что определены вне тела функции.
# Локальные - те что определены внутри тела функции

# a=0 # global
# b=0 # global
#
# def InputData1():
#     a = int(input("введите первое число ")) # local
#     b = int(input("введите второе число ")) # local

# но функции можно явно указать что она использовала глобальные переменные:

# a=0 # global
# b=0 # global
# c=0
#
# def InputData1():
#     global a,b
#     a = int(input("введите первое число ")) # теперь global - берутся из основной программы
#     b = int(input("введите второе число ")) # теперь global - берутся из основной программы
#
# InputData1() # вызвали функцию и ввели значения в глобальные переменные a и b
#
# #print("сумма сложения глобальных переменных a и b =",a+b) # отобразить сумму глобальных переменных a и b
#
# def SumData():
#     global c
#     c=a+b
#
# def PrintResult():
#     print("сумма сложения глобальных переменных a и b =",c)
#
# SumData() # вызываем функцию сложения глобальных переменных a и b
# PrintResult() # вызываем функцию вывода результата сложения глобальных переменных a и b

# НО использование глобальных переменных крайне не рекомендуется, т.к. при изменении локальных переменных на глобальные
# все функции ниже при указании тех же переменных смогут использовать теже самые переменные. Это может быть не безопасно
# т.к. другой программист может изменить значение этой переменной на свое усмотрение или случайно и в итоге программа будет работать не так как ожидалось

#------ использование return - описано в файле return.py


#--------------

# def InputData1():
#     a = int(input("введите первое число "))
#     b = int(input("введите второе число "))
#     return a,b
#
# x,y = InputData1() # записали в глобальные переменные x,y значения из локальных переменных функкции InputData1() a -> x, b -> y
#
# def Summa(n1,n2): # обьявляем аргументы, в которые будет подставлять значения из глобальных переменных x,y при вызове функции.
#     s=n1+n2
#     return s
#
# sum=Summa(x,y) # подставляем в аргументы n1,n2 значения из глобальных переменных x,y: в аргумент n1 записываем значение из глобальной переменной x, в аргумент n2 записываем значение из глобальной переменной y (n1 = x, n2 = y).
# # строку выше можно было заменить на: sum = x+y
# print("сумма двух чисел = ",sum)
#
# def Print(number):
#     print("сумма двух чисел = ",number)

#------------------------------------------------------------

# тоже самое, но кодстайл более читабельный типо

# def InputData1():
#     a = int(input("введите первое число "))
#     b = int(input("введите второе число "))
#     return a,b
#
# def Summa(n1,n2):
#     s=n1+n2
#     return s
#
# def Print(number):
#     print("сумма двух чисел = ",number)
#
# #-----main()---------
#
# x,y = InputData1()
#
# sum=Summa(x,y)
#
# Print(sum)

#--------------------------------------
# работа с аргументами



#---------- вывод значений аргументов в разном порядке

# def foo(d,e,f):
#     print(d,e,f)
#
# a,b,c = 1,2,3 # присваиваем указанным параметрам переменные и значения переменных
#
# #foo() # TypeError: foo() missing 3 required positional arguments: 'd', 'e', and 'f' (если при вызове функции без указания аргументов - для них не были указаны дефолтные значения, то будет, что не указаны аргументы)
# #foo(a,b) # TypeError: foo() missing 1 required positional argument: 'f'
# foo(a,b,c) # 1 2 3
# foo(b,a,c) # 2 1 3
# foo(c,b,a) # 3 2 1


#---------- задание для аргументов значений по умолчанию

# def foo1(d=0,e=0,f=10): # присваивание аргументам значения по умолчанию. Если функция будет вызываться без указания аргументов, то отразаятся именно эти значения для аргументов
#     print(d,e,f)
#
# a,b,c = 1,2,3 # присваиваем указанным параметрам переменные и значения переменных
#
# foo1() # 0 0 10  # если при вызове функции не передать аргументы,
# # то отобразятся эти аргументы с заданными значениями по умолчанию при описании функции.
# foo1(a,b,c) # 1 2 3
# foo1(b,a,c) # 2 1 3
# foo1(c,b,a) # 3 2 1

#-------------------

# def foo2(arg1=10,arg2=11,arg3=12): # присваивание аргументам значения по умолчанию. Если функция будет вызываться без указания аргументов, то отразаятся именно эти значения для аргументов
#     print(arg1,arg2,arg3)
#
# a,b,c = 1,2,3 # присваиваем указанным параметрам переменные и значения переменных
#
# foo2(a,arg2=b) # 1,2,12
# foo2(a,arg2=b,arg3=c) # 1,2,3
# foo2(a,b,arg3=c) # 1,2,3
#
# foo2(a) # 1 11 12
# foo2(a,c) # 1 3 12 # если не указан аргумент, то выводятся аргументы позиционные, которые заданы по умолчанию. - a,c,arg3

#--------------- *args - набор аргументов переменой длины.
# под параметр *args попадают все описанные аргументы. - a,b,c.
# При вызове функции можно вызвать как часть аргументов, так и все описанные аргументы.
# args - возвращает аргументы в виде кортежа

def foo3(*args): # присваивание аргументам значения по умолчанию. Если функция будет вызываться без указания аргументов, то отразаятся именно эти значения для аргументов
    print(args) # кортеж. Можно переделать в список, если значения аргументов надо будет поменять: print(list(args))

a,b,c = 1,2,3

foo3(a,b,c) # (1,2,3)
foo3(a,b) # (1,2)
foo3(b) # (2,)
foo3(a,c) # (1,3)

#---------------- пример операции над args после перевода в list

def foo4(*args):
    print(sum(list(args))) # вызываем функцию sum для элементов списка

a,b,c = 1,2,3

foo4(a,b,c) # 6
foo4(a,b) # 3
foo4(b) # 2
foo4(a,c) # 4
