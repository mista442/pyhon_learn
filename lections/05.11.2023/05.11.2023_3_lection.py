# a=[5,"hello",2.3, "true"] #list
# print(a)
# a=(5,"hello",2.3, True) #кортеж - tuple
# print(a[1])
# a.append("BY")
# print(a)

#ПОМЕНЯТЬ СОЖЕРЖИМОЕ КОРТЕЖА НЕЛЬЗЯ - ДАННЫЕ СОХРАНЯИЩЕСЯ В КОРТЕЖЕ - НЕИЗМЕННЫ.
#добавлять данные нельзя так же в кортеж через append
#  0   1      2    3       4
# a=(5,"hello",2.3, True, [21,17,35])
# a[4][1]=99 #для первого индекса в 4 элемента кортежа изменить 17 на 99
# #если элемент кортежа является список, то со список можно делать все что хочется
# print(a[4])
# b=a
# a[4].append(99) # добавить внутри кортежа к списку новый элемент.
# print(b[4])
# a[4].append([99,100])
# print(b[4])
#
# b=a[:] #передали данные по значению

#кортеж работает намного быстрее чем лист и занимает меньше RAM памяти

# b=[21,19,31]
# a=tuple(b)
# print(type(a))
# print(a[1])

# [] list
# () tuple
# {} dict
# {} set

#словарь - dict (ключ : значение)
#если записи повторяются, то берется последнее в словаре значение для данного ключа
# в словарь нельзя добавлять в качестве ключа листы, т.к. это изменяемый тип данных
#key - str,int,float,tuple
#value - int, string ...

# p_ages = {"Андрей": 32, "Виктор": 29, "Максим": 18, "Виктор": 35}
# print(p_ages)
#
# test = {1: 32, -1.2: 29, 37: 18, -1.2: 35}
# print(test)
#
# test1 = {(1,3): [32,10,(1,5)], "2,5": 29}
# print(test1)
#--------------------------------------------------------
# p_ages = {"Максим": 18, "Андрей": 32, "Виктор": 29, "Виктор": 35}
# p_ages = {"Максим": 18, "Андрей": 32, "Виктор": 29, "Виктор": 35}
#print(p_ages["Ольга"]) # если искать значение для несуществующего ключа, то программа будет аварийно завершена.
# для исключения несуществующих ключей есть библиотека - collection

#print(p_ages["Андрей"]) # отобразить значение ключа по имени ключа - 32
#test2=p_ages #links copy
#test2=p_ages.copy() #copy value

#p_ages["Ольга"]=18 # добавить элемент в словарь (добавляется в конц словаря)
#print(test2) #копирование происходит по ссылке
#del p_ages["Ольга"] # удалить элемент из словаря
#print(p_ages)
#------------------------------------------------------
# p_ages = {"Максим": 18, "Андрей": 32, "Виктор": 29, "Виктор": 35}
# p_ages1 = {"Максим": 33, "Андрей": 44, "Виктор": 29, "Виктор": 35}
# p_ages.update(p_ages1) #когда добавляем к одному словарю другой словать, то если ключи пересекаются, то значение из
# # нового словаря перепишет старые значения из старого словаря
# print(p_ages) # {'Максим': 33, 'Андрей': 44, 'Виктор': 35}
#--------------------------------------------------

# london_co = {
#     'r1': {
#         'hostname': 'london_r1',
#         'location': '21 New Globe Walk',
#         'vendor': 'Cisco',
#         'model': '4451',
#         'ios': '15.4',
#         'ip': '10.255.0.1'
#     },
#     'r2': {
#         'hostname': 'london_r2',
#         'location': '21 New Globe Walk',
#         'vendor': 'Cisco',
#         'model': '4451',
#         'ios': '15.4',
#         'ip': '10.255.0.2'
#     },
#     'sw1': {
#         'hostname': 'london_sw1',
#         'location': '21 New Globe Walk',
#         'vendor': 'Cisco',
#         'model': '3850',
#         'ios': '3.6.XE',
#         'ip': '10.255.0.101'
#     }
# }
# print(london_co['r1']['ios'])
# #--------------------------------------------
#
# p_ages = {"sw1": [1,2], "sw2": [1,3,4], "sw3": [7,2,5,6], "Виктор": [7,2,5,6]}

# test = {1: 3, 2: 2}
#
# a=test.__getitem__(1)
# b=test.__getitem__(2)
# c=a*b
# print(c)
#----------------------------------------------
# while - предусловие

# total = 100000
# i = 0
# while i < 5:
#     n = int(input())
#     total = total - n
#     i = i + 1
# print("Осталось", total)

# import random
#
# value = random.randint(1,36)
# #print (value)
# count=0
# flag=0
#
# while flag==0:
#     n = int(input())
#     if n == value:
#         flag=1
#         count=count+1
#     elif value >n:
#         print("загаданное число больше")
#         count=count+1
#     else:
#         print("загаданное число меньше")
#         count=count+1
# print("количество попыток", count)

# import random
#
# n = int(input("введите количество чисел\n"))
# count_user=0
# min=0
#     while count_user < n:
#         value = random.randint(1, 1000)
#     if n == value:
#         flag=1
#         count=count+1
#     elif value >n:
#         print("загаданное число больше")
#         count=count+1
#     else:
#         print("загаданное число меньше")
#         count=count+1
# print("количество попыток", count)

#-----------------------------------------------------

#множества - значения выводятся каждый раз в рандомном виде
#листы и словари не поддерживаются
#допускаются - строки, inter, кортежи
#a = {'a', 'b', 'c', 'd', 'b', 'c', 'd'}
#b = {1,2,3,4}
#c = {(1,2),(3,4)}
#d = {[1,2],[3,4]} #листы не поддерживаются
#print(a)
#print(b)
#print(c)
#print(d)
#a.add('e')
#print(a)
#a.discard('e')
#print(a)

#print()

# a = {'a', 'b', 'c', 'd', 'b', 'c', 'd',(1,2),(5,6)}
# b = {'f', 'g', 'a', 'b',(1,2),(3,4)}
# print(a)
# print(b)
# d=a&b
# print(d)