'''дана последовательность чисел, например [3,-15,10,2,5,38]
Найти min
Найти max
Найти произведение min*max
'''


# мой вариант

# def InputCountNum():
#     import random
#     a = int(input("введите количество чисел "))
#     list = []
#     for i in range(a):
#         list.append(random.randint(-10,10))
#     print(list)
#
#     return list
#
# list_n = InputCountNum() # записали сюда сгенерированный list
# def Treatment():
#     min_n = min(list_n)
#     max_n = max(list_n)
#     proizvedenie = min(list_n)*max(list_n)
#     return min_n, max_n, proizvedenie
#
# min_num, max_num, proizvedenie_num = Treatment()
#
# def Print():
#     print("минимальное число", min_num)
#     print("максимальное число", max_num)
#     print("произведение минимального и максимального числа", proizvedenie_num)
#
# Print()

# более атомарный вариант

def InputCountNum():
    import random
    a = int(input("введите количество чисел "))
    list = []
    for i in range(a):
        list.append(random.randint(-10,10))
    print(list)

    return list

list_n = InputCountNum() # записали сюда сгенерированный list

def FindMax(list_max):
    list_max.sort()
    return list_max[-1]
max_n = FindMax(list_n)

def FindMin(list_min):
    list_min.sort()
    return list_min[0]
min_n = FindMin(list_n)

def Proizvedenie(list_min,list_max):
    return list_min*list_max
proizvedenie = Proizvedenie(min_n,max_n)

def Print(min,max,proizv):
    print("min =",min)
    print("max =",max)
    print("proizvendenie min and max =",proizv)
Print(min_n,max_n,proizvedenie)
