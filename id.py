# при работе с переменными, операция присваивания может осуществлятсья по значению переменной
# или по ссылке. То есть при работе с переменными - у нее есть 2 параметра, которые ее идентифицируют:
# 1) адрес в памяти 2) значение, которое хранится в этом адресе памяти.

a=5
print("a =",a)
print("id(a) ",id(a)) #отобразить идентификатор ячейки в памяти RAM, куда сохранена переменная 'a'.

b=a #выполнили операцию пресваивания. перменные a и b будут указывать на один и тот же участок памяти. В данном
# случае операция присвания будет осуществляться по ссылке.
print("b =",b)
print("id(b) ",id(b))

print()

a=13 #при измении данных в переменной - для этой переменной будет выделяться новый участок памяти (новый id) и туда
# будет записываться информация.

print("a =",a)
print("id(a) ",id(a))

print("b =",b)
print("id(b) after change a ",id(b))