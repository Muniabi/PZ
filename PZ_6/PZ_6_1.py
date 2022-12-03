a = []

N = int(input("N:"))
for i in range(N):
    a.append(int(input("N: ")))

Temp = (a[0] > 0)
i = 1

while ((i < N) and (Temp != (a[i] > 0))):
    Temp = (a[i] > 0)
    i += 1

if i == N:
    print('0')
else:
    print(i + 1)