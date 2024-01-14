# лекция 1.6 - контроль хода выполнения программы. 12.11.2023

# ValueError
#i = int("hi") # ValueError: invalid literal for int() with base 10: 'hi'

#TypeError
#s = 8 + '3' # TypeError: unsupported operand type(s) for +: 'int' and 'str'

#ZeroDivisionError
#v = 1 / 0 #ZeroDivisionError: division by zero

flag=1 # True
while flag:
    try:
        n = int(input("введите целое число "))
        v = int(input("введите целое число "))
        s = n/v
        print(s)
        flag=0 # если программа выполнилась успешно переводим flag в 0 (False)
    except ValueError: # т.к. в блоке exept флаг не переводится в false, поэтому программа будет выполняться заново, предварительно выведя сообщение повторить попытку
        print("введено не целое число")
    except ZeroDivisionError:
        print("на ноль делить нельзя")