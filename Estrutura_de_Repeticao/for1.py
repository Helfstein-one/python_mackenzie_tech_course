numero_valido = False

while not numero_valido:

    a=int(input())

    if a <= 0:
        print("VALOR INVÁLIDO")
    else:
        numero_valido = True
        for b in range (1, a+1):
            if a % b ==0:
                print(b, end=" ")