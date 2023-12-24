'''Задача 3 Дан список некоторых целых чисел, найдите значение 20 в нем и, если оно
присутствует, замените его на 200 Обновите список только при первом вхождении числа
20'''

import random
rand_list=[]

# генерируем 10 рандомных чисел в диапазоне от 15 до 25
for i in range(10):
 a=random.randint(15,25)
 rand_list.append(a)
print(rand_list) # выводим сгенерированный компьютером лист

if 20 not in rand_list:
    print("сгенерированный список не содержит элемент с числом 20")
else:
    num=rand_list.index(20)
    value=200
    rand_list[num]=value
    print(rand_list)

