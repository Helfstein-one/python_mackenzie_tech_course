a=int(input())
if a <= 0:
    print("VALOR INVÁLIDO")
else:
    for b in range (1, a+1):
        if a % b ==0:
            print(b, end=" ")