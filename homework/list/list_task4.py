# Задача 4 Поменять местами самый большой и самый маленький элементы списка

import random

a=[] # задаем пустой список, куда будем добавлять сгенерированные компьютером числа.

for i in range(10):
    random_list=random.randint(1,100)
    a.append(random_list)

print(a)

min1=min(a)
max1=max(a)
print("\nминимальное число в индексе:",min1)
print("максимальное число в индексе:",max1)

min1_index = a.index(min1)
max1_index = a.index(max1)

print("\nиндекс минимального числа:", min1_index)
print("индекс максимального числа:", max1_index)

a[min1_index] = max1
a[max1_index] = min1

print("\nрезультат замены минимального и максимального индекса местами:")
print(a)