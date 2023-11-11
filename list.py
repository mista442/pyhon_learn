# list (список) - структура хранения данных, позволяющая хранить разные типы данных.
# Список состоит из элементов. Каждый элемент списка может быть разного типа (int,float,str,list ...)

# списки относятся к изменяемым типам данных. Данная структура является динамической.
# при попытках вывести несуществующий номер элемента в списке - будет получена ошибка (IndexError: list index out of range)

# test = [1, 'hello', 3.5, -18]
# print(test)
# print(type(test)) # тип list
#
# # вывести 2 элемент списка
# print(test[2])
#
# #----------------- методы apend и insert для работы с элементами списка ---------#
#
# # добавить в конец списка новый элемент (метод append)
# test.append(99) #после применения метода, в перенеменую добавятся новые данные
# print(test)
# print(test[4])
# #[1, 'hello', 3.5, -18, 99]
# #99
#
#
# # добавить новый элемент в указаный индекс списка (метод insert)
# test.insert(2,"world") # добавить элемент типа str со значением "world" вторым по счету индексом.
# print(test)
# #[1, 'hello', 'world', 3.5, -18, 99]
#
# # P.S. элемент с одним и тем же значением можно добавлять несколько раз и любые места в списке, например:
# test.append("cisco")
# test.insert(3,"cisco")
# print(test)
# #[1, 'hello', 'world', 'cisco', 3.5, -18, 99, 'cisco']
#
# # узнать номер индекса элемента 'world'
# print(test.index("world"))
#
# # если в списке есть несколько элементов с одним и тем же значением, при поиске номера индекса элемента - отобразится
# # только самый первый номер индекса повторяющего элемента
# print(test.index("cisco"))
#                          #3                       #7
# # #[1, 'hello', 'world', 'cisco', 3.5, -18, 99, 'cisco']
#
# # remove удаляет один элемент до первого попавшего совпадения - слева направо.
# test.remove("cisco")
# print(test)
#
# #[1, 'hello', 'world', 3.5, -18, 99, 'cisco']
#
# # pop - удалить один элемент по номеру индекса
# test.pop(6)
# print(test)
# #[1, 'hello', 'world', 3.5, -18, 99]
#
# # если номер индекса не указывать, то по умолчанию будет удален последний элемент по номеру индекса
# test.pop()
# print(test)
#
# print(test[1]) #отобразить элемент списка по номеру индекса - hello
# print(test[-3]) #отобразить элемент списка по номеру индекса - world
# print(test[1:3]) #выполнить срез элементов - ['hello','world']


#-------------- метод reverse -----------------#

#test10=[10,'hello','by',-15, 10]
#print(test10.reverse()) # делаем ревес списка - отображение в обратном порядке. Методы в листах не обязательно
# # присваивать. Они уже будут применяться без присвоения переменной. Но сам метод вывод не возвращает ни какой. Нужно
# # еще раз вывести переменную
#print(test10) # [10, -15, 'by', 'hello', 10]


#-------------- метод сount -----------------#

# посчитать сколько раз встречается указанный элемент  в списке
#print(test10.count(10)) # 2


#-------------- метод sum -----------------#

#v=[1, 2, 2, 4, 5, 4.4, 2]
#print(sum(v)) # посчитать сумму чисел указанных в элементах списка. (можно считать вместе int и float)


#-------------- метод extend -----------------#

# a=[1, -2, 2, 4, 'hello', 4.4, 2]
# b=[15,31, 'John']
# a.extend(b) # объединить список a и b вместе. Аналогично работает конкатенация при сложении типа данных str.
# print(a)
#
# #print(a+b) - команда аналогична выполнению методу a.extend(b)

#------------------- изменение данных внутри листа -------------#

# a=45
# a[0]=3
# print(a) #TypeError: 'str' object does not support item assignment - типы данных int,str,float,complex,frozen set
# относятся к неизменяемым типам данных (immutable) и поменять значение внутри переменной нельзя.

# но данные внутри листа поменять можно, т.к. это изменяемый тип данных (mutable)

#  0    1      2        #индексы элементов
a=[45, 2.1, 'hello']

#перезаписываем значение индекса элемента на новое
a[0]=35
print(a)

#------------------- лист в внутри листа ---------------------#

#        0     1       2     3          4
test = [321, 'hello', 3.5, -18, [99, 'world', -15]]
print(test)
print(type(test))
test[4][2]=-45 #переходим в 4 индекс элемента всего списка. 4 индекс это вложенный список. Далее у 2 подиндекса
# меняем значение -15 на -45

# [321, 'hello', 3.5, -18, [99, 'world', -45]]
print(test)

#---------------- добавление элемента в конец подсписка (append) ------------#

#  0   1     2        3          4
b=[15, 28, 'world', 'tank',[8, 'test', -3.5]]

# переходим в 4 индекс, и добавляем новый элемент в подсписок со значением 99
b[4].append(99)
print(b)

# --------------- добавление элемента в указаный индекс подсписка (insert) ---------------- #

# переходим в 4 индекс (это подиндекс), далее через метод insert в 1-ом подиндексе создаем элемент со значением 'world'
b[4].insert(1,'world')
print(b)

# --------------- удаление элемента подсписка по номеру индекса (pop) ---------------- #

#удалить 0 индекс в посдписке (удалить элемент со значением 8)
b[4].pop(0)
print(b)

#------------------------ сделать срез элементов внутри подсписка -------------------------#
#     0   1     2       3                  4

c = [15, 28, 'world', 'tank', ['world', 'test', -3.5, 99], 'test', 45, 'change']
print(c) #[15, 28, 'world', 'tank', ['world', 'test', -3.5, 99], 'test', 45, 'change']

#выбрать 4 элемент (подсписок). и далее внутри подсписка сделать срез с 0 по первый элементы - 'world', 'test'
print(c[4][0:2])

#------------------------ сделать срез начиная с 4 элемента и до конца всего списка

#                0    1     2       3                  4                 5     6      7
# весь список - [15, 28, 'world', 'tank', ['world', 'test', -3.5, 99], 'test', 45, 'change']

#                                    0                  1      2     3
# получится такой вывод [['world', 'test', -3.5, 99], 'test', 45, 'change']
# как видно вывод начинается с двойных скобок - теперь в выводе подсписок является началом это будет начало списка.
print(c[4:][0:])

# [4:] - выполнить срез по внутреннему списку и до конца всего списка.
# Теперь [['world', 'test', -3.5, 99], 'test', 45, 'change'] - это весь список
#[0:3] - отобразить с 0 по 2 эелементы полученного списка - [['world', 'test', -3.5, 99], 'test', 45]
print(c[4:][0:3])

#-------------------- операции присваения в листах ----------------#
# list - изменяемый тип данных. При операции присваивания для листов через новую переменную, например d=c - ссылка на
# объект c так же копируется для обьекта d. Поэтому все изменения на любую из этих переменных будет применяеться на
# обе переменные d и c.

print()

#------- через присвоение переменной ------#

#[15, 28, 'world', 'tank', ['world', 'test', -3.5, 99], 'test', 45, 'change']
print(c)
d=c
c[4][2]=-1.0
print(c)
print("id(c)", id(c)) # id одинаковые, потому что копирование по ссылке
print("id(d)", id(d)) # id одинаковые, потому что копирование по ссылке

print()

#------- через метод copy ------#

#[15, 28, 'world', 'tank', ['world', 'test', -1.0, 99], 'test', 45, 'change']

# происходит копирование по значению, а не по ссылке.
# поэтому при присвоении переменной 'е' только значение из переменной 'c' - для переменной е будет выделена новая
# ячейка памяти и будет создан новый объект для переменной e.

e=c.copy() #аналогичный результат будет если выполнить так - e=c[:] - будет так же выполнено копирование по значению
c[3]='buklya'

print("id(c)", id(c))
print("id(e)", id(e))
print("c ", c) # c  [15, 28, 'world', 'buklya', ['world', 'test', -1.0, 99], 'test', 45, 'change']
print("e ", e) # e  [15, 28, 'world', 'tank', ['world', 'test', -1.0, 99], 'test', 45, 'change']

print()
# можно изменять значения элементов внутри подсписков.

# В переменной 'с' в подиндексе пробуем поменять во 2 элементе значение с -1.0 на -50
# НО метод copy копипует по значению только для СПИСКОВ 1-ГО УРОВНЯ. Все вложенные списки будут копироваться по ссылке!!

c[4][2]=-50 # поэтому значение 2 элемента в подиндексе будет одинаковым для c и для e.

print("id(c)", id(c))
print("id(e)", id(e))
print("c ", c) # c  [15, 28, 'world', 'buklya', ['world', 'test', -50, 99], 'test', 45, 'change']
print("e ", e) # e  [15, 28, 'world', 'tank', ['world', 'test', -50, 99], 'test', 45, 'change']

print()
#---------------------------- изменение значений элементов внутри подсписка -------------------#

# например нужно в подсписке для 2 элемента изменить значение -50 на 45

# в переменную 'с' в 4 элемент (подсписок) записываем срез всех данных из переменной 'e' из подсписка.
# теперь изменения вносимые в данный подсписок для обеих переменных - будет независимым, а не копироваться по ссылке.
c[4]=e[4][:]

e[4][2]=45
print("c ", c) # c  [15, 28, 'world', 'buklya', ['world', 'test', -50, 99], 'test', 45, 'change']
print("e ", e) # e  [15, 28, 'world', 'tank', ['world', 'test', 45, 99], 'test', 45, 'change']
