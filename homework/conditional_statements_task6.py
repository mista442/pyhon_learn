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

if a == b and b == c and a == c:
    print("равносторонний треугольник")

elif (a == b and c < a and c < b) or (a == c and b < a and b < c) or (c == b and a < b and a < c):
    print("равнобедренный треугольник")

# признаки прямоугольного треугольника. По теореме Пифагора: C в квадрате =  A в квадрате +  B в квадрате.
# надо понять как записать формулу квадратного корня
if (a*a) + (b*b) = (c*c)
elif (a*a) + (c*c) = (b*b)
elif (b*b) + (c*c) = (a*a)