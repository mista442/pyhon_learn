'''
Задачи на использование словарей
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
print(ip)

unicast = int(ip[0]) >= 1 and int(ip[0]) <= 223
multicast = int(ip[0]) >= 224 and int(ip[0]) <= 239
local_broadcast = ip.count('255') == 4
unassigned = ip.count('0') == 4
#local_broadcast = int(ip[0:4]) == 255

print(int(ip.count(255)))
print(ip.count('255'))

if unicast:
    print("unicast")
elif multicast:
    print("multicast")

# count_l = 0
# local_broadcast = []
# for i in ip:
#     if int(ip[count_l]) == 255:
#         local_broadcast.append(i)
#     count_l += 1
#
#
# count_u = 0
# unassigned = []
# for i in ip:
#     if int(ip[count_u]) == 0:
#         unassigned.append(i)
#     count_u += 1

elif local_broadcast:
    print("local broadcast")
elif unassigned:
    print("unassigned")
elif not unicast and not multicast and not local_broadcast and not unassigned:
    print("unused")




