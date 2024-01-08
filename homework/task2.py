'''
Задание 2: Сделать копию скрипта задания 1 Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
• состоит из 4 чисел (а не букв или других символов)
• числа разделенны точкой
• каждое число в диапазоне от 0 до 255
Если адрес задан неправильно, выводить сообщение: «Неправильный IP-адрес».
Сообщение «Неправильный IP-адрес» должно выводиться только один раз, даже если
несколько пунктов выше не выполнены.
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


ip = str(input("введите ip адрес "))
ip = ip.split('.')
if len(ip) != 4:
    print("ne to")
    quit()
octet = 0
correct_ip = []
if len(ip) == 4:
    for i in ip:
        if int(ip[octet]) >= 1 or int(ip[octet]) <= 255:
            correct_ip.append(i)
            octet += 1
            print(correct_ip)
            print(len(correct_ip))
        else:
            print(correct_ip)
            print("ne to2")
            exit()


print(correct_ip)
if int(ip[0]) >= 1 and int(ip[0]) <= 223:
    print("unicast")
elif int(ip[0]) >= 224 and int(ip[0]) <= 239:
    print("multicast")
elif ip.count('255') == 4:
    print("local broadcast")
elif ip.count('0') == 4:
    print("unassigned")
else:
    print("unused")




