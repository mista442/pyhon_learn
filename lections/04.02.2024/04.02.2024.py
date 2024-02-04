# 11.02 - 08.30
# 18.02 - не будет занятия
# 25.02 - 13:30
# 03.08 - не будет занятия
# 17.03 ?
# 24.03 - онлайн

#------ повторение

# print('hello',end=' test') # hello test
# print()
#
# # f = open('result.txt','w') # если файла нет, то он будет создан. 'w' - write
# # for num in range(10):
# #     print(f'item {num}',file=f)
# # f.close()
#
# print(list(range(2,10)))
#
# list_of_words = ['one', 'two', 'list', '', 'dict']
# print(sorted(list_of_words))
#
# list_of_value = [3, 2, 9, 5] # сортировка для разных типов данных не доступна [3, 'one', 2, 9, 5]
# print(sorted(list_of_value))
#
# list_of_month_template=['январь','февраль','март','апрель','май','июнь','июль','август']
# list_of_month = ['март', 'август', 'январь', 'апрель']
# list_res=[]
# for iter in list_of_month_template:
#     if iter in list_of_month:
#         list_res.append(iter)
# print(list_res)
#
# from operator import itemgetter
# list_of_list = [[1,9,2],[8,2],[190,1]]
# print(sorted(list_of_list, key=itemgetter(1)))
#
# # функция map позволяет сделать операцию с каждым элементом - как цикл for
#
# numbers = [1, 2, 4, 5, 7, 8, 10, 11]
# def  filter_odd_num(in_num):
#     if in_num>=3 and in_num<=8 :
#         return True
#     else:
#         return False
# out_filter = filter(filter_odd_num, numbers)
#
# print("Тип объекта out_filter: ", type(out_filter))
# print("Отфильтрованный список: ", list(out_filter))

#--------- модули для написания сетевых скриптов

import os
import shutil
# вывести текущую директорию. Не важно какая ОС
print("Текущая деректория:", os.getcwd())

#os.makedirs('folder') # создание директории с названием folder

print(os.listdir()) # отобразить содержимое в текущем каталоге. как ls в линуксе.

# os.mkdir("One")
# print(os.listdir())
# os.makedirs("Two/qqq")
# print(os.listdir())
# print(os.listdir("./Two/"))

#shutil.rmtree('Two') # удаление папки и вложенных файлов/папок - как rm -rf
#os.rmdir('Two')

# import os
# import shutil
# # вывести текущую директорию
# print("Текущая деректория:", os.getcwd())
# os.mkdir("One")
# print(os.listdir())
# os.makedirs("Two/qqq1")
# os.makedirs("Two/qqq2")
# print(os.listdir())
# print(os.listdir("./Two/"))
# os.rmdir("Two/qqq2")
# print(os.listdir("./Two/"))
# text_file = open("./Two/qqq1/text.txt", "w")
# text_file.write("Это текстовый файл")
# print(os.listdir("./Two/qqq1"))
# shutil.rmtree("Two/qqq1")
# print(os.listdir("./Two/"))

#os.rename('old_name_file','new_name_file') # переименовать файл

import ipaddress

ipv4 = ipaddress.ip_address('10.0.1.1')
print(ipv4)

#-----------
print()

import ipaddress
ip1 = ipaddress.ip_address('10.0.1.1')
ip2 = ipaddress.ip_address('10.0.2.1')
print(ip1 > ip2)
print(ip2 > ip1)
print(ip1 == ip2)
print(ip1 != ip2)
print(str(ip1))
print(int(ip1))
print(ip1 + 5)
print(ip1 - 5)

#-------------
print()

import ipaddress
subnet1 = ipaddress.ip_network('80.0.1.0/28')
print(subnet1.broadcast_address)
print(subnet1.with_netmask)
print(subnet1.with_hostmask)
print(subnet1.prefixlen)
print(subnet1.num_addresses)
print(list(subnet1.subnets()))

#-----------------
print()

import ipaddress
subnet1 = ipaddress.ip_network('192.168.1.0/24')
print(subnet1.broadcast_address)
print(subnet1.with_netmask)
print(subnet1.with_hostmask)
print(subnet1.prefixlen)
print(subnet1.num_addresses)
print(list(subnet1.subnets()))
for ip in subnet1:
  print(ip)
print("subnet[10]", subnet1[10])

#--------------------------------------

from tabulate import tabulate
sh_ip_int_br = [('FastEthernet0/0', '15.0.15.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.12.1', 'up', 'up'),
 ('FastEthernet0/2', '10.0.13.1', 'up', 'up'),
 ('Loopback0', '10.1.1.1', 'up', 'up'),
 ('Loopback100', '100.0.0.1', 'up', 'up')]
print(tabulate(sh_ip_int_br))