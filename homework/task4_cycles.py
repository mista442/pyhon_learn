'''
Задание 4: Написать программу – игра - угадай, в которой с помощью функции random
генерируется случайное число от 1 до 50 Пользователю предлагается угадать данное
число, на основе подсказать – загаданное число больше или меньше числа пользователя.
Вывести число попыток отгадывания числа
'''

import random
value = random.randint(1,50)

print("Угадайте целое число от 1 до 50. \nНеограниченное количество попыток. Lets go.")

user_try = 0 # количество попыток пользователя
user_int = int # ввод числа пользователем

while user_int != value:
    user_try = user_try + 1
    user_int=int(input("\nВведите число "))

    if user_int == value:
        print("Вы угадали число!! Yep! :)")
        print("Сделано попыток угадать число: ",user_try)
    elif user_int > value:
        print("Введите число меньше.","Сделано попыток угадать число: ",user_try)
    elif user_int < value:
        print("Введите число больше.","Сделано попыток угадать число: ",user_try)