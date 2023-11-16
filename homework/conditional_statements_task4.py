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
    a1,b1,c1=int(input("длина ")),int(input("высота ")),int(input("ширина "))

    if a1 <=0 or b1 <=0 or c1 <=0:
        print("\nвведите параметры размера ящика равными > 0\n")
    else:
        flag1=False

if a1 > a and b1 > b1 and c1 > c:
    print()

    print("\nкоробка влезает в ящик")
else:
    print("\nкоробка не влезает в ящик")
