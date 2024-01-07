'''
Задание 2: Сделать копию скрипта задания 1. Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
• состоит из 4 чисел (а не букв или других символов)
• числа разделенны точкой
• каждое число в диапазоне от 0 до 255
Если адрес задан неправильно, выводить сообщение: «Неправильный IP-адрес».
Сообщение «Неправильный IP-адрес» должно выводиться только один раз, даже если
несколько пунктов выше не выполнены.
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

try:
    ip = str(input("введите ip адрес "))
    ip = ip.split('.') # строку переделываем в список, в качестве разделителя элементов указываем точку.

    check_ip = []
    if len(ip) != 4:
        print("не то")
        quit() # выходим из программы если проверка на введение корректного ip адреса не пройдена
    else:
        if len(ip) == 4:
            for i in ip:
                if int(i) >= 0 or int(i) <= 255:
                    check_ip.append(i)
        print(check_ip)


            unicast = int(ip[0]) >= 1 and int(ip[0]) <= 223
            multicast = int(ip[0]) >= 224 and int(ip[0]) <= 239
            local_broadcast = ip.count('255') == 4
            unassigned = ip.count('0') == 4

            if unicast:
                print("unicast")
            elif multicast:
                print("multicast")
            elif local_broadcast:
                print("local_broadcast")
            elif unassigned:
                print("unassigned")
            elif not unicast or not multicast or not local_broadcast or not unassigned:
                print('unused')
except:
    print("Неправильный IP-адрес")

