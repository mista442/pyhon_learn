import random
value = random.randint(1,100)

print("Угадайте целое число от 1 до 100. \nНеограниченное количество попыток. Lets go.")
print("\nВведите число")

i = 0
v = 0
a = 0
while a != value:
    v = v + 1
    a=int(input())

    i = i + 1

    if a == value:
        print("Вы угадали число!! Yep! :)")
    elif a > value:
        print("Введите число меньше.","Количество попыток угадать число: ",v)
    elif a < value:
        print("Введите число больше.","Количество попыток угадать число: ",v)