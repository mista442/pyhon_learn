# Напишите  программу  (файл  user.py),  которая  запрашивала  бы  у
# пользователя:
# •имя (например, "What is your name?")
# •возраст ("How old are you?")
# •место жительства ("Where are you live?")
# •После этого выводила бы три строки:
# •"This is имя"
# •"It is возраст"
# •"(S)he live in место_жительства"
# •Вместо  имя,  возраст,  место_жительства  должны  быть  данные,
# введенные пользователем.

name = input("What is your name? : ")
age = input("How old are you? : ")
place = input("Where are you living? :")

print()

print(f"My name is {name}")
print(f"I'm {age}")
print(f"I'm living in {place}")