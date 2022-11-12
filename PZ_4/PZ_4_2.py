import random

N = random.randrange(1,100)

print('N = ', N)

K = 1
S = 1

while S <= N:
    K += 1
    S += K
    print("K = {0}, S = {1}". format(K,S))

S -= K
K -= 1
print()
print("K = {0}, S = {1}". format(K,S))