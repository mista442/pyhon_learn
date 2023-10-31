a='a kto eto sdelal?'

print("a =",a)
print("type a is",type(a))
d=a.split('o') #функция split в питоне создает разделитель и делает из строки - список (list). Аналогично как awk -F ''.
# дока про split - https://docs.python.org/3.3/library/stdtypes.html?highlight=split#str.split
# В данном случае, в качестве разделителя будет указана буква 'o'.
# В значении всей строки, где встречается буква 'o' - она будет удаляться и после нее будет ставится запятая.
# по умолчанию в split используется в качестве разделителя пробел



print("d=a.split('o')")
print("d = ",d) # ['a kt', ' et', ' sdelal?']
print(type(d)) # теперь тип данных поменялся - стал list вместо str.
#---------------------------------------------
print()

b='1,2020,45,october,salary'
print("b =",b)
print("type b is",type(b))
c=b.split(",")
print("c=b.split(',')")
print("c =",c) # ['1', '2020', '45', 'october', 'salary']
print("type c is",type(c))
#----------------------------------------------
print()

a='1,,2,,3,,4,,5,,6'
print("a = a='1,,2,,3,,4,,5,,6'")
print(a.split(",",-4))
print(a)