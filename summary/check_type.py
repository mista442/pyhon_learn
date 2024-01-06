#метод .isdigit()
# чтобы проверить, состоит ли строка из одних цифр, можно использовать метод isdigit. Метод возвращает значение True/False.

a = "a100"
a1 = "aaa"
a2 = "100"
a3 = "100 1"

print(a.isdigit()) # False
print(a1.isdigit()) # False
print(a2.isdigit()) # True
print(a3.isdigit()) # False

#--------------------------
print()

#метод .isalpha()
# чтобы проверить, состоит ли строка из одних букв, можно использовать метод isalpha. Метод возвращает значение True/False.

a = "a100"
a1 = "aaa"
a2 = "100"
a3 = "aaa a"

print(a.isalpha()) # False
print(a1.isalpha()) # True
print(a2.isalpha()) # False
print(a3.isalpha()) # False

#--------------------------

# type - вернуть значение типа переменной

a = 10
a1 = 'a'
a2 = [1,2,3]
a3 = (1,3,3)
a4 = {1:1,2:2,3:3}
a4 = {1,2,3}
a5 = [a,a1,('test','test2')]

a6 = [a,a1,a2,a3,a4,a5]

for i in a6:
    print(type(i))

#вывод будет такой:
# <class 'int'>
# <class 'str'>
# <class 'list'>
# <class 'tuple'>
# <class 'set'>
# <class 'list'>