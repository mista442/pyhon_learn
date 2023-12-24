# # функция map - работа с каждым элементом списка. По сути аналог цикла for
#
# list_of_str = ['1', '2', '5', '10']
# print(list(map(int, list_of_str))) # переделываем каждый эл списка из str в int
# #[1, 2, 5, 10]
#
# dict_of_str = {1:'1', 2:'2', 3:'5', 4:'10'}
# list_1 = list(map(int, dict_of_str))
# print(list_1)
#
# # фнукция zip
#
# employee_numbers = [2, 9, 18, 28]
# employee_names = ["Дима", "Марина", "Андрей", "Никита"]
# zipped_values = zip(employee_names, employee_numbers)
# print(zipped_values)
# zipped_list = list(zipped_values)
# print(zipped_list)
# print(type(zipped_list[0]))
#
#
# employee_numbers = [2, 9, 18, 28]
# employee_names = ["Дима", "Марина", "Андрей", "Никита"]
# zipped_values = zip(employee_names, employee_numbers)
# zipped_list = dict(zipped_values)
# print(zipped_list)
#
#
# employee_numbers = {2:3, 9:18, 18:8, 28:29}
# employee_names = ["Дима", "Марина", "Андрей", "Никита"]
# zipped_values = zip(employee_names, employee_numbers)
# zipped_list = set(zipped_values)
# print(zipped_list)

#---------------

# def filter_odd_num(in_num):
#     if (in_num % 2) == 0:
#         return True
#     else:
#         return False
#
#
# numbers = [1, 2, 4, 5, 7, 8, 10, 11]
# out_filter = filter(filter_odd_num, numbers)
# print("Тип объекта out_filter: ", type(out_filter))
# print("Отфильтрованный список: ", list(out_filter))

#--------------

# c = map(lambda x:x+x,filter(lambda x: (x>=3), (1,2,3,4)))
# lambda x:x+x - для элемента выполнить элемент(х) + элемент(х)
# filter(lambda x: (x>=3), (1,2,3,4)) - отфилтровать элементы. вывести только те, которые больше или равны 3.
# map - выполнить для каждого элемента

# print(list(c)) # преобразовать вывод в лист

#--------------

# import re # подключение библиотеки регулярных выражений
# regex = re.compile('\s+')
# regex_num = re.compile('\d+')
# код предмента, сокращенное название предмета, полное название предмета
#text = """100 ИНФ  Информатика 2130  МАТ  Математика 15689    АНГ Английский"""
#text = """ИНФ  Информатика 2130  МАТ  Математика 15689    АНГ Английский"""
#print(re.split('\s+', text))
#print(regex.split(text))
# print(regex_num.search(text).start())
# print(regex_num.search(text).end())
#print(regex.sub(' ',text)) # найти значения из переменной regex и заменить ее на один пробел.

# regex1 = re.compile('\s+\W\s+')
# text = """100 , ИНФ .  Информатика  ! 2130 ?  МАТ :  Математика 15689    АНГ Английский"""
#print(text1)
#print(regex1.sub(' ',text1)) # найти значения из переменной regex и заменить ее на один пробел.


# print(re.findall('[0-9]+', text))
# # извлечь все коды курсов (для латиницы [A-Z])
# print(re.findall('[А-ЯЁ]{3}', text))
# # извлечь все названия курсов
# print(re.findall('[а-яА-ЯёЁ]{4,}', text))

#------------ модули


# print(sys.builtin_module_names)

# import adder # подключили файл(модуль) к проекту. Положил в папку с проектом.
# import adder2
# #print(sys.path)
# #from adder import add # импортировать только функцию add из модуля adder
# import sys
#
# #s=adder.name
# #print(s)
# adder.name="Hello" # изменяет название модуля только на время работы программы - в самом файле ничего не поменяется.
# print(adder.name)
# nums_summ = adder.add(5,10) # adder - указание модуля, add - вызвали имя функции, в скобках параметры с которыми выполняем функцию.
# print(nums_summ)
#
# nums_summ = adder2.add(5,10) # adder - указание модуля, add - вызвали имя функции, в скобках параметры с которыми выполняем функцию.
# print(nums_summ)
#
#
# nums_raznost = adder.subtraction(10,5)
# print(nums_raznost)

# def hi(name="yasoob"):
#     print("Вы внутри функции hi()")
#
#     def greet():
#         return "Вы внутри функции greet()"
#
#     def welcome():
#         return "Вы внутри функции welcome()"
#
#     print(greet())
#     print(welcome())
#     print("Вы внутри функции hi()")
#-----------------main---------------
# hi()
# Вывод: Вы внутри функции hi()
#        Вы внутри функции greet()
#        Вы внутри функции welcome()
#        Вы внутри функции hi()
#----------------------------------------
# def hi(name="yasoob"):
#     def greet():
#         return "Вы внутри функции greet()"
#     def welcome():
#         return "Вы внутри функции welcome()"
#     if name == "yasoob":
#         return greet
#     else:
#         return welcome
# a = hi()
# print(a)
# # Вывод: <function greet at 0x7f2143c01500>
#
# print(a())
# Вывод: Вы внутри функции greet()

# def hi():
#     return "Привет yasoob!"
#
# def doSomethingBeforeHi(func):
#     print("Я делаю что-то скучное перед исполнением hi()")
#     print(func())
#
# #----------main--------------
# doSomethingBeforeHi(hi)
# Вывод: Я делаю что-то скучное перед исполнением hi()
#        Привет yasoob!

#--------------------------------------------------------------

def decorator_function(wrapped_func):
    def wrapper():
        print('Входим в функцию-обёртку')
        print('Оборачиваемая функция: ', wrapped_func)
        print('Выполняем обёрнутую функцию...')
        wrapped_func()
        print('Выходим из обёртки')
    return wrapper
@decorator_function
def hello_world():
        print('Hello world!')

#---------------main-------------
hello_world()