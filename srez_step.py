#[START:STOP:STEP]

a='hello world'
print(a[::2]) #отобразить каждый второй символ

# .   .   .   .   .   .   #hlowrd
# 0 1 2 3 4 5 6 7 8 9 10
# h e l l o   w o r l d

#можно так еще записать
print(a[::1+1])

print(a[::-2]) #перевернуть вывод - drwolh