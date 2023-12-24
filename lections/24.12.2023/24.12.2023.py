# 7 января не занимаемся, 14 января в 13:30

# тема - классы, модификаторы

#  модификаторы доступа - public, private, protected.
#  public используется по умолчанию. Разрешен доступ всем и когда угодно.
#  private - доступ разрешен только внутри класса. __ - модификатор private (двойное нижнее подчеркивание)
#  protected - одинарное нижнее подчеркивание. Доступ к этому полю пользователю запрещен. Доступ разрешен только внутри класса и дочерним классам (наследование).

class Person:
    def __init__(self, name, age=0): # названия входных аргументов
        self.name = name # public - можно получить доступ когда и где угодно
        self.__age = age # private - доступ вне класса запрещен. Разрешено только внутри класса.

    def _display(self):
        print(self.name)
        print(self.__age)

    def getAge(self): # read only age
        print(self.__age)

    def setAge(self, age): # write age
        self.__age = age

# name, age - это атрибуты

person = Person('Dev', 30)
#person.__aqe= -31
#print("person.age ",person.__age)

person.display()
# person.display() выведет name и __age на каждой новой строчке
# Dev
# 30

person.setAge(35) # задаем возраст - поменяли 30 на 35
person.getAge() # возвращаем результат печати возраст (35)

person1 = Person('Sergey')
person1.display() # а если бы в 13 строчке было бы: def __display(self), то мы получили бы ошибку - AttributeError: 'Person' object has no attribute 'display'.
# то есть использовать этот метод вне класса запрещено.