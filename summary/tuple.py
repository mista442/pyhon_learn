# # tuple - это кортеж.
# # кортеж представляется собой аналогичную структуру списка - имеет набор элементов, которые могу содержать разные типы данных.
# # Но сам кортеж является неизменяемым типом данных.
# # то есть элементы кортежа изменить нельзя. Элементы кортежа заносятся в круглые скобки
#
# # [] - list (лист)
# # () - tuple (кортеж)
#
# a=(1, 2.2, "test", -8)
#
# #но если внутри кортежа есть вложенные структуры данные, которые можно изменять - то их можно изменить
#
# a=(1, 2.2, "test", -8, [10,-5, 'hello'])
# print(type(a))
# print(type(a[4])) # 4 элемент кортежа можем изменить, т.к. он является типом данных - list.
#
# a[4].append(99)
#
# # [10, -5, 'hello', 99]
# print(a[4])
#
# # т.к кортеж является неизменяемым типом данных,
# # то присваивашие кортежа в через новую переменную будет осуществляться по ссылке
# b=a
# print("id(a)",id(a))
# print("id(b)",id(b)) # the same id like 'a'
#
# print(b)
#
# c=b[:]
#
# print("id(c)",id(c))
# print("id(b)",id(b)) # the same id like 'c'
#
# # НО копирование по срезу выполняет копировние по значению только внешней структуры данных. Все вложенные структуры данных будут копироваться по ссылке!! (актуально для любых структур хранения, не только для tuple. В любых структурах хранения - вложенные структуры хранения данных будут копироваться по ссылке через срез)
# # поэтому если надо скопировать по значению, то нужно выполнить срез их другой переменной, где эта вложенная струкетура данных находится
#
# # c = (1, 2.2, 'test', -8, [10, -5, 'hello', 99])
# print()
#
# #c[4]=b[4][:] # но так не работает. TypeError: 'tuple' object does not support item assignment.
# # 27:33 на этой минуте про это говриться в 3_lection_листы_кортежы_множества_05.11.23_1.mp4

# как вариант на вопрос выше из видео - переделать b в list и потом сделать в нужный индекс b срез из нужного индекса переменной a:

#-------
# a=(1, 2, 3, [10, 'hello', -2.1])
# b=a[:] # или так b=list(a[:]), тогда строка ниже b = list(b) - не нужна будет.
# print(a) # (1, 2, 3, [10, 'hello', -2.1])
# print(b) # (1, 2, 3, [10, 'hello', -2.1])
#
# b = list(b) # теперь b стал типом данных - list.
# # Когда делали b=a[:], то короче и проще было бы сразу на этапе среза переменной сказать что это будет тип данных list, а не делать это потом. Так - b=list(a[:])
# print(b) # [1, 2, 3, [10, 'hello', -2.1]]
#
# # т.к b теперь это структура данных list, то можем ее изменить.
# # для b берем в 3 индекс кортежа, который является вложенной структурой данных list и пишем в него срез из вложенной структуры данных индекса 3 переменной a.
# b[3] = a[3][:]
#
# b[3][1] = 'test'
#
# print(id(a[3]))
# print(id(b[3]))
#
# b = tuple(b)
#
# print(a)
# print(b)
#---------

# #----------------------------- размер данных в переменной----------------
#
# #листы занимают больше места чем кортежы.
#
# print()
#
a1=[1,2,3]
b1=(1,2,3)
#
c1=[1,2,3,4,10,24,'hello',2.3,15]
d1=(1,2,3,4,10,24,'hello')
#
print(a1.__sizeof__()) # вывести размер данных в переменной a1
print(b1.__sizeof__())
print(c1.__sizeof__())
print(d1.__sizeof__())
#
# #---------------------- изменения типа данных
#
# a2=[1,2,3]
# b2=tuple(a2)
#
# print()
#
# print(id(a2))
# print(id(b2))
#
# a2[1]=22
#
# print("type b2 =", type(b2)) # tuple
# print(b2) # (1,2,3)
# print("type a2 =", type(a2)) # при этом a2 остается типом list
# print(a2) # [1,22,3]
#
# #-------------
# print()
#
# a3=[1,2,3,[10,11,12]]
# b3=tuple(a3)
#
# print()
#
# print(id(a3))
# print(id(b3))
#
# a3[3][2]=221 # list внутри кортежа передается по ссылке. изменения сделанные списке переменной a - так же применяться и для списка переменной b.
#
# print("type b3 =", type(b3)) # tuple
# print("type b3[3] =", type(b3[3])) # list
# print(b3) # (1,2,3)
# print("type a3 =", type(a3)) # при этом a2 остается типом list
# print(a3) # [1,22,3]
#
# #------------------- переделка типа данных list в tuple
# print()
#
# l=[45,18,21,'hello']
# print("id l before convert",id(l))
# l=tuple(l)
# print(type(l))
# print("id l after convert", id(l)) # выделяется новый участок памяти для переменной l, т.к. теперь это новый тип данных
# # и т.к. tuple < чем list по обьему памяти. Поэтому tuple в list запихнуть не получится. Нужен новый участок памяти.
#
# # ну и соответвенно можно тип данных переделать обраьно из кортежа в лист. И конечно, встроенные структуры останутся неизменными.
# l=list(l)
# print(l)

#в кортеж можно добавить вложенные структуры данных - на этапе создания кортежа:
#1. через перечисление элементов кортежа в исходном виде
# a=(1,2,3,['hello',15,-2.3])

#2. или через указание переменной в качестве элемента кортежа, в которой хранятся вложенные структуры данных
# b=['test','go',123]
# c=(10,11,'hello',b,11)
# print(c) # (10, 11, 'hello', ['test', 'go', 123],11)

# print(id(b))
# print(id(c[3])) # т.к ссылки одинаковые, то все изменения в листе "b" применятся так же для листа, вложенного в кортеж "c"

#-----------------методы кортежей
# print()

# узнать номера индекса элемента в кортеже - отобразит до первого попавшего совпадения
# (10, 11, 'hello', ['test', 'go', 123],11)
# print(c.index(11)) # 1

# отобразить количество указанных элементов первого уровня (во внутренние структуры хранения функция не лазиет)
# print(c.count(11))

# посчитать сумму чисел в кортеже
#print(sum(c)) # но это работает только для 1 уровня стурктуры хранения.
# Для вложенных структур хранения функция суммы не работает. И работает только для типа данных int и float

# v=(1,2,3,5.6)
# print(sum(v))

# del v # удалить кортеж 'a'

