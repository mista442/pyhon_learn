#из 3 чисел заданных пользователем - найти максимальное число.

print("введите 3 числа")
a,b,c=int(input()),int(input()),int(input())

# 1. a = b = c
if a == b and b == c and c == a:
    print('все числа равны -', a)

# 2. a > b and a > c
elif a > b and a > c:
    print(a,"наибольшее число")

# 3. b > a and b > c
elif b > a and b > c:
    print(b,"наибольшее число")
# 4. c and b > c
elif c > a and c > b:
    print(c,"наибольшее число")

# 5. a == b and a,b > c
elif a == b and a > c and b > c:
    print(a,"наибольшее число")

# 6. a == c and a,c > b
elif a == c and a > b and c > b:
    print(a,"наибольшее число")

# 7. b == c and b,c > a
elif b == c and b > a and c > a:
    print(b,"наибольшее число")

#print(a,"",b,"",c,"")