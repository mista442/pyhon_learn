'''задачу решали в классе! - task3 '''

def cylinder(R, H):
    pi = 3.14

    def circle():
        S = pi * R * R
        print(f"Площадь круга по формуле πr2 = : {S} см2")
        return S

    temp = circle()
    S2 = 2 * pi * R * H
    Sfull = temp * 2 + S2
    a = int(input("введите 1 - площадь боковой поверхности, введите 2 - полная площадь "))
    if a == 1:
        print(f"Площадь боковой поверхности цилиндра {S2} см2")
    elif a == 2:
        print(f"Полная площадь цилиндра {Sfull} см2")
    else:
        print("Введите цифру 1 или 2")

        cylinder(5, 5)