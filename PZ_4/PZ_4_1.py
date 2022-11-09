A = int(input()) #Ввод А
B = int(input()) #Ввод B

if A<B:
    for i in range(A+1, B):
        print(i)

else:
    for i in range(A-1, B, -1):
        print(i)
