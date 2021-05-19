def valorPagamento(vp, da):
    prest = vp
    if da == 0:
        return prest
    else:
        dia_atr = da
        mt = prest * 0.03
        jr_atr = (dia_atr * (0.1 / 100)) * prest
        tot = prest + mt + jr_atr
        return tot

def main():
    valor = float(input())
    dias = int(input())
    print(valorPagamento(valor, dias))

main()







