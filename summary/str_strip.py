# по умолчанию метод strip убирает символы переноса строки, табуляцию, пробелы, новые строки. В этот набор входят
# \t\n\r\f\v

a1='\n\tinterface FastEthernt0/1\n'
print(a1)

b1=a1.strip()
print(b1)