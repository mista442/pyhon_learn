# 4. Напишите программу, которая определяет пройдет коробка с размерами a*b*c в ящик с размерами x*y*z

flag=True
while flag:
    print('введите размеры коробки:')
    a,b,c=int(input("длина ")),int(input("высота ")),int(input("ширина "))

    if a <=0 or b <=0 or c <=0:
        print("\nвведите параметры размера коробки равными > 0\n")
    else:
        flag=False

print()

flag1=True
while flag1:
    print('введите размеры ящика:')
    x,y,z=int(input("длина ")),int(input("высота ")),int(input("ширина "))

    if x <=0 or y <=0 or z <=0:
        print("\nвведите параметры размера ящика равными > 0\n")
    else:
        flag1=False

if (x > a and y > b and z > c) and (x > b and x > c) and (z > a and z > b):

    print("\nкоробка влезает в ящик")
else:
    print("\nкоробка не влезает в ящик")
