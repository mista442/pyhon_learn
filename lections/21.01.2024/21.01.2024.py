# FIO_List = ['Иванов','Петров','Яблочкин','Грушин','Ласточкин']
# Algebra = [3,4,5,5,4]
# Fisica = [2,4,4,5,3]
# Russian = [2,5,5,5,2]
# Class = ['10a','10b','10a','10b','10v']

Ivanov = ['Иванов',3,2,2,'10а']
Petrov = ['Петров',4,4,5,'10б']
Yablochkin = ['Яблочкин',5,4,5,'10а']
Grushin = ['Грушин',5,5,5,'10б']
Lastochkin = ['Ласточкин',4,3,2,'10в']

Fio = [Ivanov,Petrov,Yablochkin,Grushin,Lastochkin]


classes = [Ivanov[-1],Petrov[-1],Yablochkin[-1],Grushin[-1],Lastochkin[-1]]
set_classes = set(classes)
classes = list(set_classes)
print(classes)

def Object(n,surname):
    l=[]
    for i in surname:
        if isinstance(i,int):
            l.append(i)
    if min(l) == n:
        print(surname[0])

def Grade_2(n,surname):
    if surname.count(n) == 1:
        print(surname[0])

def Mnogo_4(surname):
    if 4 in surname:
        print(surname.count(4))

print("Cписок хорошистов, у кого оценки по предметам не ниже 4:\n")
for i in Fio:
    Object(4,i)
print("\nCписок школьников, у которых всего одна 2:\n")
for i in Fio:
    Grade_2(2,i)
print("\nКласс в которых больше всего хорошистов:\n")
for i in Fio:
    Mnogo_4(i)



# Object(4,Ivanov)
# Object(4,Petrov)
# Object(4,Yablochkin)
# Object(4,Yablochkin)
