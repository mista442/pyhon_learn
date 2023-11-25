'''
пользователь вводит количество чисел, например 10
number = int(input("введите количество чисел"))
компьютер генерируется number случайных, каждое в диапазоне от 1 до 1000.

найти max среди сгенерированных чисел
найти min среди сгенерированных чисел
найти среднее среди сгенерированных чисел
найти количество четных и нечетных чисел
'''

import random
num = int(input("введите количество чисел\n"))

count = 0
gen_list=[]
while count < num:
    value = random.randint(1, 1000)
    gen_list.append(value)
    count = count + 1
print(gen_list, "- числа сгенерированные компьютером\n")

gen_list.sort()
print(gen_list[0],"минимальное число")
print(gen_list[len(gen_list)-1],"максимальное число")
print(sum(gen_list)/len(gen_list),"среднее значение ряда чисел")

count_index=0
chet=0
nechet=0
while count_index < len(gen_list):
    if gen_list[count_index] % 2 == 0:
        chet = chet + 1
    elif gen_list[count_index] % 2 != 0:
        nechet = nechet + 1
    count_index = count_index + 1

print("количество четных чисел",chet)
print("количество нечетных чисел",nechet)

#---------------------------------------------------------------
'''
пользователь вводит количество чисел, например 10
number = int(input("введите количество чисел"))
компьютер генерируется number случайных, каждое в диапазоне от 1 до 100.

найти max среди сгенерированных чисел
найти min среди сгенерированных чисел
найти среднее среди сгенерированных чисел
найти количество четных и нечетных чисел
'''
# import random
# num = int(input("введите количество чисел\n"))
#
# count = 0
# s=0 #сумма
# min=100
# max=1
# while count < num:
#     value = random.randint(1, 100)
#     print("value",value)
#     if value > max:
#         max == value
#     elif value < min
#     s=s+value
#     print("s+value",s)
#     count = count + 1
# print("s",s)