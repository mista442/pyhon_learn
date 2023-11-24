a=5
print("a =",a*10)
print(type(a)) # определить тип данных

a="5"
print("a =",a*10) #питон будет просто дублироваить строку 10 раз
print(type(a)) # определить тип данных

b=12.6
print("b =",b*10)
print(type(b))

#c=a+b неявное преобразование типов string + float.
c=float(a)+b #явно указываем что 'a' это теперь float а не string
print("с =",c)
print(type(c))