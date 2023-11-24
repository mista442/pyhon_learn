import random
value = random.randint(1,100)

print("Угадайте целое число от 1 до 100. \nВсего 6 попыток.")
print("\nВведите число")

i = 0
v = 6
while i < 6:
    v = v - 1
    a=int(input())

    i = i + 1

    if a == value:
        print("Вы угадали число!! Yep! :)")
    elif i == 6:
        print("Вы не угадали число! :((")
    elif a > value:
        print("Введите число меньше.","Осталось",v,"попыток")
    elif a < value:
        print("Введите число больше.","Осталось",v,"попыток")