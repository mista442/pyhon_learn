# cпособы как подпрограмма передавать данные из тела функции для основной программы:

# - использование глобальных переменных
# - использование return
# - использование файлов
# - передача аргументов по ссылке

#------ использование return

# ------ пример 1 - без использования return -------------------------------------------------------------

# def InputData1():
#     a = int(input("введите первое число "))
#     b = int(input("введите второе число "))
#
# InputData1() # ничего не выведется
# # Внутри функции не объявлен print результата выполнения боди или return для сохранения значений в вызове функции. Поэтому ничего не увидим.
#
# # ------ пример 2 - только для вывода результата (print), --------------------------------------------------
# # но никуда дальше не получиться использовать вывод результата для других функций или main программ.
# # Т.к. функция print только позволяет вывезти результат выполнения и ничего больше
#
# def InputData2():
#     a = int(input("введите первое число "))
#     b = int(input("введите второе число "))
#     print(a,b)
#
# InputData2() # отобразятся значения локальных переменных a и b из функции InputData2

# ------- пример 3 - запись выполнения функции в новую переменную через функцию return ----------------------------

# def InputData3():
#     a = int(input("введите первое число "))
#     b = int(input("введите второе число "))
#     return a,b
#
# x = InputData3() # записываем результат return в новую переменную
# print(x) # значения переменных a и b в виде кортежа (почему в кортеж пишется не оч понятно, видимо чтобы потом нельзя было отадаываемые данные сходу поменять)
# print(type(x)) # <class 'tuple'>

# ------ пример 4 - запись выполнения функции в новую переменную через команду return и в рамках return как-то обработать возвращаемые данные ------

# def InputData4():
#     a = int(input("введите первое число "))
#     b = int(input("введите второе число "))
#     return a+b # в рамках return как-то складываем возвращаемые переменные a и b
#
# x = InputData4() # записываем результат обработки return в новую переменную
# print(x) # вывод переменной x
# print(type(x)) # <class 'int'>


# ------ пример 5 - возвращаем введенные переменные и эти переменные записываем в новые глобальные переменные ------

def InputData5():
    a = int(input("введите первое число "))
    b = int(input("введите второе число "))
    return a,b # возвращаем a и b

x,y = InputData5() # x = a, y = b
print(x,y)