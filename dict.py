# {} dict - словарь
# словарь хранит данные формата - ключ : значение

# типы данных, которые могут принимать ключ и значение
# key может хранить - str,int,double,tuple (только неизменяемы типы данных)
# value может хранить - str,int,double,tuple,list (и те и другие)

#если ключи в словаре повторяются, то берется последнее в словаре значение для данного ключа ("Виктор": 18)
p_ages = {"Андрей": 32, "Виктор": 29, "Максим": 18, "Виктор": 18}
print(p_ages) # {"Андрей": 32, "Виктор": 18, "Максим": 18}

# ключ -2 дублируется, поэтому при выводе словаря - отобразится ключ -2 со значением 8.
p_ages1 = {1:1, -2:3.2, 19.2:1, -2:8, 'hello':10.1, 'test':'rere'}
print(p_ages1) # {1:1, -2:8, 19.2:1, 'hello':10.1, 'test':'rere'}

p_ages2 = {(1,2):"test", 10:5.1,('hello',10,2.2):8}
print(p_ages2)

# в словарь нельзя добавлять листы в качестве ключа, т.к. это изменяемый тип данных
#p_ages3 = {[1,2,3]:'test'}

# но листы можно использовать в качестве значения
p_ages4 = {(1,2,3):['test',1,2.5]}
print(p_ages4)

#------------ данные из другой перменной использовать в качестве значения ключа

list1 = [1,2,3]
a = {'test':10, 48:'hello', 1:23}
a = {'test':list1, 48:'hello', 1:23} # данные копируются по ссылке при указании переменной в качестве значения ключа

print(a) # a = {'test': [1, 2, 3], 48: 'hello', 1: 23}

list1[1] = 55 # list1 = [1,55,3]
a = {'test':list1[:], 48:'hello', 1:23} # a = {'test': [1, 55, 3], 48: 'hello', 1: 23}
list1[1] = 70 # list1 = [1,70,3]

# данные в ключ test скопированы по значению, по этому теперь изменения в list1 и в значении ключа test независимы друг от друга
print(a) # a = {'test': [1, 55, 3], 48: 'hello', 1: 23}

print(id(list1))
print(id(a['test'])) # [1, 55, 3]
print(list1) # [1,70,3]
print(a['test']) # [1, 55, 3]






