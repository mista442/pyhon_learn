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
