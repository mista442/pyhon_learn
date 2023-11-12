# a="world hello world friend"
# print(a.find("friend")) # метод find ищет номер символа в строке - 12. И так же
#
# s='FastEthernet/0/{}'
# print(s.format(2)) # функция format подставляет в фигурные скобки указанное значение
import setuptools.command.build_ext

# vlan, mac, intf = ['100', 'aabb.cc80.7000', 'Gi0/1'] # записали в указанные переменные значения элементов из списка
# print("{:>15} {:>15} {:>15}".format(vlan, mac, intf)) # формат вывода сообщений
#
# ip_template = '''
# IP address:
# {}
# mask
# {}
# '''
# print(ip_template.format('10.1.1.1','/24'))

# ip_template = '''
# IP address:
# {ip}
# mask
# {mask}
# '''
# print(ip_template.format(ip='10.1.1.1',mask='/24'))
# print(ip_template.format(mask='/24',ip='10.1.1.1'))

# flag=True
# while flag:
#   try:
#     a = int(input('Введите 1 целое число: '))
#     b = int(input('Введите 2 целое число: '))
#     c=a/b
#     print(type(c))
#     print("Все нормально. ", c)
#     #flag=False
#   except:
#     print("Вы ввели не целое число")
#   #except ZeroDivisionError:
#   #  print("делить на ноль нельзя")
#   else:
#     flag=False

    #------------- цикл for

    # два типа циклов for - с итератором и с возможностью изменения

# spisok = [10, 40, 20, 30]
# for element in spisok:
#   print(element + 2)
#
# print(spisok)

# count=0
# for count in range(len(spisok)): # range(4) 0 1 2 3. функция range создает последовательный счетчик. В данном случае о длины списка.
#   spisok[count]=spisok[count]+5
# # count=count+1
#
# print(spisok)
#
# i = 0
# for element in spisok:
#     spisok[i] = element + 2
#     i += 1
#
# print(spisok)

# for i in range(10):  # 0 1 2 ...9
#   print(f'interface FastEthernet0/{i}')
#
# vlans_list = [10, 20, 30, 40, 100]
# vlans_dict = {10:"aaa", 20:"bbb", 30:"ccc", 40:"ddd", 100:"fff"}
#
# for vlan in vlans_dict:
#    print(vlans_dict[vlan])
#    print(f'vlan {vlan}')
#    print(f' name VLAN_{vlan}')

#Даны два списка
# list_1=[10,20,30,40,50,40,40]
# list_2=[10,15,20,10,30,35,40,45,50,40,45]
# Сформировать третий список из общих элементов первых двух
# [10,20,30,40,]
#замечание: использование множеств ЗАПРЕЩЕНО!!!

# for count_1 in range(len(list_1)):
#      for count_2 in
#      #if count_1 == list_2[0]:
#
#      list_all = []
#      for count_1 in range(len(list_1)):  # count_1=0
#          for count_2 in range(len(list_2)):  # count_2=0  1   2 3   4 5
#              if list_1[count_1] == list_2[count_2]:
#                  if not list_1[count_1] in list_all:
#                      list_all.append(list_1[count_1])
#      print(list_all)
#
# list_all=[]
# for element in list_1:
#     if (element in list_2) and (not element in list_all):
#         list_all.append(element)
# print(list_all)

#------------------------------------

#Дан список
#       0   1  2  3 4  5  6     count_1
# list_1=[10,20,10,20,30,10,30,40]
# # подсчитать сколько раз встречается каждый элемент
# #10 - 3, 20 - 2, 30 - 2
# # замечание: использование множеств ЗАПРЕЩЕНО!!!
# list_2=[]  # используется для хранения не повторяющихся элементов
# for element in list_1:
#     if not element in list_2:
#         list_2.append(element)
# print(list_2)
#
# for element in list_2:
#     print(element)
#     print(list_1.count(element))

#------------------------------------

#Дан список
#       0   1  2  3 4  5  6     count_1
list_1=[21,22,23,24,25,26,27, 28]
# пользователь вводит два числа, например 5,  2
# вывести все значения списка которые делятся на первое число ИЛИ на второе число
# ИЛИ на разницу чисел 5 - 2 = 3

#замечание: использование множеств ЗАПРЕЩЕНО!!!

# 21,22,24,25,25,27,28

flag=True
while flag:
    try:
        print("введите два целых числа")

        num1=int(input())
        num2=int(input())

        list_2=[]

        for elm in list_1:

            if elm % num1 == 0 or elm % num2 == 0 or elm % (num1-num2) == 0:
                list_2.append(elm)
        print(list_2)
    except ZeroDivisionError:
      print("делить на ноль нельзя")
#    else:
#       flag=False
  #------------------------------------

  # # # Дан список
  # # #       0   1  2  3 4  5  6     count_1
  # list_1 = [21, 22, 23, 24, 25, 26, 27, 28]
  # # # пользователь вводит два числа, например 5,  3
  # # # вывести все значения списка которые деляться на первое число или на второе число
  # # # или на разницу чисел 5 - 2 = 3
  # print(list_1)
  # a = int(input("введите первое число "))
  # b = int(input("введите второе число "))
  # d = a - b
  # #
  # for element in list_1:
  #     if element % a == 0 or element % b == 0 or element % d == 0:
  #         print(element)


