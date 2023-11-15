import random
value = random.randint(1,10)

flag=True
while flag:
    print("введите число")
    a=int(input())

    if a == value:
        print("вы угадали число")
    elif a > value:
        print("введенное число больше загаданного")
    elif a < value:
        print("введенное число меньше загаданного")
flag=False