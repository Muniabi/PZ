import random #импортируем библиотеку рандом

N = random.randrange(2,11) #количество цифр в списке
a = [random.randrange(1,11) for i in range(N)] #цифры в списке
b = []

print("N:",N)
print("Список a:\n",a)

for i in range(0,N) :
    if a[i]%2 == 0 :
        b.append(a[i])

print("Размер масива b:\n",len(b)) #количество символов в cписке b
print("Список b:\n",b)