# a=5
# print("a =",a*10) # a = 50
# print(type(a)) # определить тип данных - <class 'int'>
#
# a="5"
# print("a =",a*10) #питон будет просто дублировать строку 10 раз - a = 5555555555
# print(type(a)) # определить тип данных - <class 'str'>
# #
# b=12.6
# print("b =",b*10) # b = 126.0
# print(type(b)) # <class 'float'>
# #
# # c=a+b неявное преобразование типов string + float. Но складывать строки и вещественные числа нельзя.
# # будет такая ошибка - TypeError: can only concatenate str (not "float") to str
# c=float(a)+b #явно указываем что 'a' это теперь float а не string
# print("с =",c) # с = 17.6
# print(type(c)) # <class 'float'>

#----------- ввод данных в строку

# t=input("введите строку\n")
# print("вы ввели:",t)

#----------- метод .strip

# # по умолчанию метод strip убирает символы переноса строки, табуляцию, пробелы, новые строки. В этот набор входят
# # \t\n\r\f\v
#
# a1='\n\tinterface FastEthernt0/1\n'
# print(a1)
#
# b1=a1.strip()
# print(b1)

#----------- функция split

# a='a kto eto sdelal?'
#
# print("a =",a) # a = a kto eto sdelal?
# print("type a is",type(a)) # type a is <class 'str'>
# d=a.split('o') #функция split в питоне создает разделитель и делает из строки - список (list). Аналогично как awk -F ''.
# # дока про split - https://docs.python.org/3.3/library/stdtypes.html?highlight=split#str.split
# # В данном случае, в качестве разделителя будет указана буква 'o'.
# # В значении всей строки, где встречается буква 'o' - она будет удаляться и после нее будет ставится запятая.
# # по умолчанию в split используется в качестве разделителя пробел
#
#
#
# print("d=a.split('o')")
# print("d = ",d) # ['a kt', ' et', ' sdelal?']
# print(type(d)) # теперь тип данных поменялся - стал list вместо str.
# print(d[1]) # вывести второй список индекса из листа. Выведется ' et'.
#
# print()
# #list (список) - структура хранения данных, позволяющая хранить разные типы данных. Каждый элемент списка может быть
# # разного типа (int,float,str,list ...)
#
# test = [1, 'hello', 3.5, -18]
# print(test)
#
# print(test[2]) # вывести 2 элемент списка
#
#
#
# #---------------------------------------------
# print()
#
# b='1,2020,45,october,salary'
# print("b =",b)
# print("type b is",type(b))
# c=b.split(",")
# print("c=b.split(',')")
# print("c =",c) # ['1', '2020', '45', 'october', 'salary']
# print("type c is",type(c))
# #----------------------------------------------
# print()
#
# a='1,,2,,3,,4,,5,,6'
# print("a = a='1,,2,,3,,4,,5,,6'")
# v=a.split(",",3) # 3 - значит в качестве разделителя удалить первые три запятые.
# print(v) # ['1', '', '2', ',3,,4,,5,,6']
# print(v[1]) #ничего не выведется, т.к второй индекс в листе ничего не содержит - ''
# v=a.split(",",3)
# print(v)
# print(v[1]) #ничего не выведется, т.к второй индекс в листе ничего не соредржит - ''
# print(v[-1]) # отобразить последний элемент списка # ,3,,4,,5,,6
#
# s='Hello my friend!'
# l=s.split(" ") # создали из строки список с отдельными элементами
# print(l) # ['Hello', 'my', 'friend!']
# print(l[0]) # Hello

#--------------- метод .replace

# #метод replace заменеят указанное значение в подстроке на другое
#
# a='FastEthernet0/1'
# print(a)
#
# b=a.replace('Fast','Gigabit')
# print(b) #GigabitEthernet0/1

# i = '1,2,2,1,3,4,5,6,2'
# print(i.replace('2','10')) # 1,10,10,1,3,4,5,6,10

#--------------- метод .find

#метод find() по указанному значению ищет подстроку в строке и возвращает первый индекс  найденной подстроки.
#если указанная подстрока не найдена, то метод вернут ошибку -1.

#                    11
# t o d a y  i s  a  g o o d  w e a t h e r

# a='today is a good weather'
# b=a.find('good')
# print(b) # 11

#--------------- метод .join

# метод join() выполняет обратное действие методу split. Он формурует из списка строку.
# метод join отвечает за объединение списка строк c помощью определенного указателя.

# spisok=["10", "23", "31", "40"]
# print(spisok)
# print(type(spisok))
#
# a1="-".join(spisok) # если не укзаывать "-" - то результат будет 10233140. Вот так a1="".join(spisok)
# print(a1) # 10-23-31-40 (тип str)
# print(type(a1)) # str

# ------------ метод .format

# специальный символ {} указывает куда подставить указанное значение из .format(value).
# Значения можно подставлять разного типа (int,str,list...)

# i = str(input("укажите номер интерфейса "))
# interface = 'FastEthernet0/{}'
# print(interface.format(i))
#
# i2 = str(input("укажите номер интерфейса "))
# p2 = str(input("укажите номер порт "))
# interface2 = 'FastEthernet{}/{}'
# print(interface2.format(i2,p2))

# ip_template = '''
# IP address: {ip} mask: {mask}
# '''
# print(ip_template.format(ip='10.1.1.1',mask='/24')) # IP address: 10.1.1.1 mask: /24
