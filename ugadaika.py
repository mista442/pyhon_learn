import random
value = random.randint(1,10)

flag=True
while flag:
    print("введите число")
    a=int(input())

    if a == value:
        print("вы угадали число")
        flag = False
    elif a > value:
        print("введите число меньше")
    elif a < value:
        print("введите число больше")
flag=False