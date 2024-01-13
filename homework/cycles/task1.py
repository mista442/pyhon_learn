'''
Задание 1: Запросить у пользователя ввод IP-адреса в формате 10.0.1.1. Ввод данных
осуществляется в виде строки. В зависимости от типа адреса (описаны ниже), вывести на
стандартный поток вывода:
• «unicast» - если первый байт в диапазоне 1-223
• «multicast» - если первый байт в диапазоне 224-239
• «local broadcast» - если IP-адрес равен 255.255.255.255
• «unassigned» - если IP-адрес равен 0.0.0.0
• «unused» - во всех остальных случаях
'''

ip = str(input("введите ip адрес "))
ip = ip.split('.')

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
