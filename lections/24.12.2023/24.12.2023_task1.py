'''
Реализовать класс целых чисел, выполнить реализацию методов ввода данных, поиска данных,
удаление данных,вывода данных, сложение список
Пример
class MyList
a = MyList(1,2,3,4)
b=MyList(4,5,5)
b.Find(5)   #номера индексов  1  2
b.Add(6)   #b  [4,5,5,6]
b.Remove(7)  #операция не допустима
d=a+b  [1,2,3,4]  + [4,5,5,6]   [5,7,8,10]
'''

import random

class MyList:
    def __init__(self):
        self.__spisok=[] #что бы пользователь в дальнейшем не мог этот список изменять

    def RandomInput(self):
        n=random.randint(5,5)
        for i in range(n):
            self.__spisok.append(random.randint(1,100))

    def ManualInput(self):
        n=int(input("введите количество чисел "))
        for i in range(n):
            self.__spisok.append(int(input("введите число ")))

    def PrintSpisok(self):
        if len(self.__spisok) > 0:
            print(self.__spisok)
        else:
            print("список пустой")

    def AddItem(self):
        self.__spisok.append(int(input("введите число ")))
    def RemoveItem(self):
        if len(self.__spisok) > 0:
            value=int(input("введите число для удаления "))
            p=self.__spisok.count(value)
            if p>0:
                for i in range(p):
                    self.__spisok.remove(value)
            else:
                print("числа", value, "нет в списке")

    def __add__(self, other):
        temp=MyList()
        if len(self.__spisok) > 0 and len(self.__spisok) == len(other.__spisok):
            for i in range(len(self.__spisok)):
                temp.__spisok.append(self.__spisok[i]+other.__spisok[i])
            return temp
        else:
            print("сложение не возможно")

a=MyList()
b=MyList()
a.RandomInput()
b.RandomInput()
a.PrintSpisok()
# b.ManualInput()
b.PrintSpisok()

#d = MyList()
#d=a
# a.AddItem()
# a.AddItem()
# a.PrintSpisok()
# a.RemoveItem()
# a.PrintSpisok()
#d.PrintSpisok()

#d=MyList
d=a+b
d.PrintSpisok()
