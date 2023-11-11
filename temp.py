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

# цикл for с счетчиком цикла


# Задание: посчитать все Hello
a = (5,'Hello', 2.3, True,[21,17,'Hello',35],'Hello', ('By', 'Hello'))
# Считаем сколько Hello у нас в кортеже без учета вложенных списков и кортежей
helloCount = a.count('Hello')
# Проходим в цикле по всем элементам и проверяем не является ли элемент списком/кортежем
for iter in a:
    # Если элемент является списком/кортежем, то считаем сколько в нем Hello и суммируем с найденым ранее
    if type(iter) == list or type(iter) == tuple:
        helloCount = helloCount + iter.count('Hello')

print('Hello найдено', helloCount, 'штуки')


