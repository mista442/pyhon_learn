'''Задача 6 Дан список в виде списка списков, например [[1,2,3],[2,6,4],[3,4,5],[6,3,7]].
Вывести список из элементов списка – без повторения, результат– [1,2,3,6,4,5,7]. Вывести
списков из элементов списка, которые повторяются в исходном списке, результат –
[2,3,4,6]'''

a=[[1,2,3],[2,6,4],[3,4,5],[6,3,7]]
print(a)
b=[] # пустой список куда буду складывать только уникальные числа

list_count_indexes = len(a) # сколько всего вложенных листов в общем списке
count_next_index = 0


count_index = 0 # счетчик для одного индекса подписков - [1,2,3] - первый индекс списка, [2,6,4] - второй индекс списка и т.д.
el_count = 0 # счетчик для элементов внутри вложенного списка

next_podspisok = 0 # счетчик для элементов в каждом нового списка

count_el_podspisok = len(a[next_podspisok])

while el_count < count_el_podspisok:
    print(a[count_index][el_count])
    if a[count_index][el_count] not in b:
        b.append(a[count_index][el_count])
    el_count += 1
    if el_count == count_el_podspisok:
        el_count = 0
        count_index +=1
        next_podspisok +=1
        if count_next_index == list_count_indexes:
            break
    print(b)