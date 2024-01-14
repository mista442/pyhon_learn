#l = [15,11,22,3]

# варианты задания цикла for: 1) range, 2) через просто итератор (пройдется по всем элементам списка), 3) с искуственным счетчиком

# 1) range
# for i in range(len(l)): # range(4): 0 1 2 3. Функция range при указании len генерирует числа по умолчанию от 0 до числа len (4). Но можно и любой другой диапазон. range(-10,4) - от -10 до 4.
#     print(l[i])

# for i in range(0,2): # вывести с 0 по 1 элементы
#     print(l[i]) # 15 11
#
# print()
#
# for i in range(2,4): # вывести с 2 по 3 элементы
#     print(l[i]) # 22 3

# 2) just iter.
# for i in l: # аналогично циклу выше. i будет заходить в каждый элемент списка
#     print(i+3)

# 3) counter. c += 1
# c=0
# for i in l: # аналогично циклу выше. Переменная 'c' будет сдвигать элемент в каждой итерации
#     print(l[c])
#     c += 1

#---------- словари в цикле

vlans_dict = {'vlan_floor1': 10,'vlan_floor2': 20,'vlan_floor3': 30,'vlan_floor4': 40}

    #key       #value
for vlan_name, vlan_id in vlans_dict.items():
    print(f' interface FastEthernet0/{vlan_id}')

 # interface FastEthernet0/10
 # interface FastEthernet0/20
 # interface FastEthernet0/30
 # interface FastEthernet0/40

for key in vlans_dict:
    print(vlans_dict[key]) # отобразить значения ключей. vlans_dict - переменная, хранящая словарь. А key итератор для ключей при выполнении цикла.

    # 10
    # 20
    # 30
    # 40

