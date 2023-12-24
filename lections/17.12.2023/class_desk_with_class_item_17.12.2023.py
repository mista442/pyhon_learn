class Item:
    def __init__(self):
        self.name = input("Введите название предмета")
        self.s = int(input("Введите площадь предмета"))

    def Print(self):
        print("Название предмета ", self.name)
        print("площадь предмета ", self.s)


class DeskTable:

    def __init__(self):
        self.length = int(input("Введите длину стола"))
        self.width = int(input("Введите ширину стола"))
        self.high = int(input("Введите высота стола"))
        self.color = input("Введите цвет стола")
        self.current_s = self.length * self.width
        self.list = []

    def Print(self):
        print("Длина стола", self.length)
        print("Ширина стола", self.width)
        print("высота стола", self.high)
        print("цвет стола", self.color)
        print("свободная площадь стола ", self.current_s)
        for iter in self.list:
            # print("Список вещей на столе",self.list)
            iter.Print()

    def CountS(self):
        return (self.length * self.width)

    # -	создайте метод изменения длины прямоугольника с проверкой на положительное значение и с проверкой на число (вводить буквы - нельзя)
    def SetColor(self, color_new):
        self.color = color_new

    def SetLength(self, length_new):
        if isinstance(length_new, int) and (length_new > 0) and (length_new >= self.width):
            self.length = length_new
        else:
            print("операция не может быть выполнена из-за ввода недопустимых значений")

    def AddItem(self, Item):
        if (self.current_s >= Item.s):
            self.list.append(Item)
            self.current_s = self.current_s - Item.s
        else:
            print("объект ", name, " разместить на столе нельзя")

    def DeleteItem(self, name, s1):
        if (name in self.list):
            self.list.remove(name)
            self.current_s = self.current_s + s1
        else:
            print("такого объекта ", name, " нет на столе ")
        # -------------main----------


a = DeskTable()
a.Print()

# color_new=input("Введите цвет стола")
# a.SetColor(color_new)

# length_new=input("Введите новую длину стола")
# a.SetLength(length_new)
# a.Print()
b = Item()
a.AddItem(b)
# a.AddItem("TV2", 3)
a.Print()

# a.DeleteItem("TV3", 3)
# a.Print()
