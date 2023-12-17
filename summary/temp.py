# a="privet kak dela?"
#
# # 0  1  2  3  4  5  6  7 8 9 10 11 12 13 14 15
# # p  r  i  v  e  t     k a k     d  e  l  a  ?
# #16 15 14 13 12 11  10 9 8 7  6  5  4  3  2  1    #со знаком минус
# print(a[7:10]) #kak
#
# print(a[7:]) #kak dela?
# print(a[-9:]) #kak dela?
# print(a[:-1]) #privet kak dela
# print(a[:-11]) #prive
# print(a[:-10],a[15:]) #privet ?
# print(a[7:-10]) #left - k dela?, right - privet. Результатом будет ничего
#
# print(a[:-11]) #prive
# print(a[-7:]) #k dela? - начиная с минус седьмого символа до конца (до минус первого)
#
#
# #left n положительное: отобразить с указанного номера символа - слева направо до конца строки
# print(a[7:]) #kak dela?
#
# #left n отрицательное: отобразить с указанного номера символа - слева направо до конца строки
# print(a[-9:]) #kak dela?
#
# #right n положительное: отобразить с указанного номера символа - слева направо до конца строки
# print(a[:11]) #privet kak (включая пробел после kak): отобразятся слева направа - первые 10 символов.
#
# #right n отрицательное: отобразить с указанного номера символа - слева направо до конца строки
# print(a[:-1]) #privet kak dela
# print(a[:-11]) #prive

#------------------------------------------------------

# b="Gamburgernaya ulitsa"
# # 0   2   4   6   8
# # G a m b u r g e r n a y a   u l i t s a
# #        -15           -8  -6  -4  -2  -1
#
# #c 0 до 19
# #или -1 до -20
#
# print(b[3:8]) #burge
# print(b[15:-10]) #пусто
# print(b[:9]) #Gamburger
# print(b[14:]) #ulitsa - не верно
# print(b[-3:-7]) #a ulitsa - не верно
# print(b[-15:8]) #urge - не верно
#                       6
# a=[1, 2, 2, 4, 5, 4, [2, 2], 2]
# b=a[:]
#
# print(id(a))
# print(id(b))
# # print(b.count(2))

#--------------------------------------

# a=int(input("длина "))
# b=int(input("ширина "))
# c=int(input("высота "))
#
# print(a,"",b,"",c,"")

# аналогично эти команды можно записать в 2 строки:

# a,b,c=int(input("длина ")),(input("ширина ")),(input("высота "))
# print(a,'',b,'',c,'')

# a=list(input("длина ширина высота\n"))
# print(a)

# print('введите размер ящика:')
# a,b,c=int(input("высота ")),int(input("ширина ")),int(input("глубина "))
# print(a,'',b,'',c,'')
# print()
#
# print('введите размеры двери:')
# x,y=int(input("высота ")),int(input("ширина "))
# print(x,'',y,'')
#
# if x<=a and y<=b:
#     print("YES")
# else:
#     print("NO")

#---------------------------------------

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

#Дан список
#       0   1  2  3 4  5  6     count_1
# list_1=[21,22,23,24,25,26,27, 28]
# # пользователь вводит два числа, например 5,  2
# # вывести все значения списка которые делятся на первое число ИЛИ на второе число
# # ИЛИ на разницу чисел 5 - 2 = 3
#
# #замечание: использование множеств ЗАПРЕЩЕНО!!!
#
# # 21,22,24,25,25,27,28
#
# flag=True
# while flag:
#     try:
#         print("введите два целых числа")
#
#         num1=int(input())
#         num2=int(input())
#
#         list_2=[]
#
#         for elm in list_1:
#
#             if elm % num1 == 0 or elm % num2 == 0 or elm % (num1-num2) == 0:
#                 list_2.append(elm)
#         print(list_2)
#     except ZeroDivisionError:
#       print("делить на ноль нельзя")

#       1     3               8
# a = [10,11,12,11,13,13,45,76,11]
# for i in a:
#     print(a.index(11))

# b=0
# a=50
# n=98
# if n == 100:
#     b = n + a
# print(b)

# while True:
#     print('hello')

# total = 100
# i = 0
# while i < 5:
#     n = int(input())
#     total = total - n
#     i = i + 1
# print("Осталось", total)


# s='hello w'
# print(s+'orld')

# floor1 = {
#     'Sw0':{
#         'vendor':'cisco',
#         'mac':'aa-bb-cc',
#         'ip':'192.168.88.10',
#         'ios':'15.4'
#     },
#     'Sw1': {
#         'mac': 'bb-cc-dd',
#         'ip': '192.168.89.10',
#         'ios': '15.4',
#         'vendor': 'cisco'
#     },
#     'Sw2': {
#         'mac': 'cc-dd-ee',
#         'ip': '192.168.90.10',
#         'ios': '15.4',
#         'vendor': 'cisco'
#     }
# }
#
# print(floor1.get(input("введите название устройства ")))

a=[1, 2.2, "test", -8, (10,-5, 'hello')]
print(a)

#a[4][2] = 'test'

#print(a)