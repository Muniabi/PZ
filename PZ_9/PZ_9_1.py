from statistics import mean
a = []

def temp ():
  N = int(input("Введите количество месяцев:"))
  for i in range(N):
      a.append(int(input("Введите температуру каждого месяца:")))
  F = mean(a)
  print("Средняя температура за год:",F)
  print("Минимальная температура:",min(a))

temp()