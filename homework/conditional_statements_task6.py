'''Напишите программу, которая у пользователя запрашивает три числа
определяющие стороны треугольника. Определить тип треугольника: равнобедренный,
равносторонний, прямоугольный, обычный'''

flag=1
while flag:
    print("введите стороны треугольника")

    a=int(input())
    b=int(input())
    c=int(input())

    if a <=0 or b <=0 or c <=0:
        print("каждая из сторон треугольника должна быть > 0")
    else:
        flag=0

not_treugolnik = a + b > c and a + c > b and b + c > a
ravnostoroniy = a == b and b == c and a == c
ravnobedreniy = (a == b and c < a and c < b) or (a == c and b < a and b < c) or (c == b and a < b and a < c)
pryamougolniy = ((c*c) == (a*a) + (b*b)) or ((b*b) == (a*a) + (c*c)) or ((a*a) == (b*b) + (c*c))

if not_treugolnik:
    print("введенные параметры не характеризуют треугольник")

elif ravnostoroniy:
    print("равносторонний треугольник")

elif ravnobedreniy:
    print("равнобедренный треугольник")

elif pryamougolniy: # c=6, a=6, b=8. Теорема Пифагора: (c*c) == (a*a) + (b*b). По ней считаем прямоугольный треугольник.
    print("прямоугольный треугольный")

elif not ravnostoroniy or ravnobedreniy or pryamougolniy or not_treugolnik:
    print("произвольный треугольник")
