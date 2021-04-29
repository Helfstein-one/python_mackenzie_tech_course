numero_valido = False

while not numero_valido:

    a = int(input())

    if a < 0 or a > 10:
        print("VALOR INVÁLIDO")

    else:
        numero_valido = True
        for d in range(1, 11, 1):
            print(f'{a}x{d}={a*d}')