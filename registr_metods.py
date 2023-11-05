#методы upper,lower,swapcase,capitalize выполняют преобразование регистра строки.
# upper - переводит регистр всех символов в заглавные буквы
# lower - переводит все символы в строчные буквы
# swapcase - меняет регистр каждого символа на противоположный
# capitalize - делает самый первый символ в строке заглавным, остальные символы строчными



a='FastEthernet'
b=a.upper() # FASTETHERNET

print(b)

c=a.lower() # fastethernet
print(c)

d=a.swapcase() # fASTeTHERNET
print(d)

e=a.capitalize() # Fastethernet
print(e)

v='TunNelL hello hOW are You'
n=v.capitalize() # Tunnell hello how are you
print(n)