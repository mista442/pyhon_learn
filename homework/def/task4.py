"""Задача 4 Дан список целых чисел. Посчитать, сколько раз в нем встречается каждое
число. Например, если дан список [1, 1, 3, 2, 1, 3, 4], то в нем число 1 встречается три раза,
число 3 - два раза, числа 2 и 4 - по одному разу."""

# создать пустой список, добавить в него уникальные элементы из изначального списка
# уникальный список переделать в словарь и в качестве значения ложить количество элементов из изначального списка

#надо добавить сортировку сначала

l = [1, 1, 3, 2, 1, 3, 4]
#def count_num():
#    global l
# c=0
# # l_uniq = []
dict1 = {}
l1 = []

for i in l:
    if i not in l1:
        l1.append(i)
    #if i == l.index(i-1):
    #    continue
print(l1)
    # l.count(i)
    # c = c + 1
    #print("число",i,"встречается",l.count(i),"раз")

c=0
for i in l1:
    print(l.count(l1.count(i)))