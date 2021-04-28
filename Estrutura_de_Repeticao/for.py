a=int(input())
if a < 0 or a > 10:
    print("VALOR INVÁLIDO")
else:
    for b in range (1,11, 1):
        print(f'{a}x{b}={a*b}')


