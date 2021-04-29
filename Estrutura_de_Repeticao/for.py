a=int(input())
if a < 0 or a > 10:
    print("VALOR INVÁLIDO")
else:
    for d in range(1, 11,):
    print(f'{a}x{d}={a*d}')


