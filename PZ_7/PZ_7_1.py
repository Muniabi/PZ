import random
# Получаем рандомное число в диапазоне который задан. Для примера K1 будет равен рандомному числу от 1 до 21,
# N1 будет равен рандомному числу в диапазоне от 1 до рандомного числа K1 к которому добавили 
K1 = random.randrange(1,21)
N1 = random.randrange(1,K1+1)
S1 = input()
K2 = random.randrange(1,21)
N2 = random.randrange(1,K2+1)
S2 = input()

#выводим строки и их длину
print("N1:",N1)
print("K1:",K1)
print("S1:",S1)
S1_length = len(S1)
print("Длина S1:",S1_length)

print()
print("N2:",N2)
print("K2:",K2)
print("S2:",S2)

S2_length = len(S2)
print("Длина S2:",S2_length)

# работа со срезами по индексам
S1_new = S1[:N1]
S1_new_length = len(S1_new)
print("\nНовая строка S1:",S1_new)
print("Новая длина S1:",S1_new_length)

S2_new = S2[-N2:]
S2_new_length = len(S2_new)
print("\nНовая строка S2:",S2_new)
print("Новая длина S2:",S2_new_length)
print("\nНовая строка:",S1_new+" "+S2_new)
