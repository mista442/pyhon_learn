# классы

# class Car:
#     #указывать модификаторы доступа - public, private, protected
#     # create class attributes
#     name = "c200"
#     make = "mercedez"
#     model = 2008
#
#     # create class methods
#     def start(self):
#         print ("Engine started")
#
#     def stop(self):
#         print ("Engine switched off")
# #------------main--------
# car_a = Car()  # car_a - переменные, экземпляры класса
# car_b = Car()
#
# print("Car.name ",Car.name)
# Car.name="s500"
# print("Car.name ",Car.name)
# #print("car_a.name ",car_a.

#--------------------------------------------------

class Car:
    # create class attributes
    car_count = 0
    # create class methods
    def start(self, name, make, model):
        print ("Engine started")
        self.name = name # атрибут экземпляра
        self.make = make # атрибут экземпляра
        self.model = model # атрибут экземпляра
        Car.car_count += 1
    def add_color(self, color):
        self.color = color  # атрибут экземпляра
    def PrintColor(self):
        print("color car ", self.color)
    def PrintC(number):
        # print("color car ", self.color)
        print("car_count ", Car.car_count)
        print("number ", number)

Car.PrintC(17)

#------------main ------------
car_a = Car()
car_a.start("Corrola", "Toyota", 2015)

print(car_a.name)
car_a.add_color("white")
print(car_a.color)
#print(car_a.car_count)
car_a.PrintColor()

car_b = Car()
car_b.start("City", "Honda", 2013)
print(car_b.name)
car_b.color="black"
print(car_b.color)
print(car_b.car_count)

#----------------------

class Rectangle:
    def __init__(self):
        self.length = int(input("Введите длину прямоугольника"))
        self.width = int(input("Введите ширину прямоугольника"))

    def Print(self):
        print("Длина прямоугольника", self.length)
        print("Ширина прямоугольника", self.width)

    def CountP(self):
        return (self.length + self.width) * 2

    def CountS(self):
        return (self.length * self.width)


def SetLength(self, length_new):
    if isinstance(length_new, int) and (length_new > 0):
        self.length = length_new
    else:
        print("операция не может быть выполнена из-за ввода недопустимых значений")


# -------------main----------
a = Rectangle()
a.Print()
print("Периметр прямоугольника ", a.CountP())
a.SetLength(13)
a.Print()


"""
Написать класс – письменный стол. Учитывая следующие рекомендации:
- создайте метод __init__(), внутри которого будут определены следующие динамические свойства: ширина, длина, высота, цвет Начальные значения свойств берутся из входных параметров метода.
Добавить список объектов на столе List
•	создайте метод print() – вывод на экран параметры письменного стола– ширина-высота, длина, цвет, 
•	создайте метод PrintS  - который возвращает площадь рабочей поверхности 
•	создайте метод параметра пись
"""

