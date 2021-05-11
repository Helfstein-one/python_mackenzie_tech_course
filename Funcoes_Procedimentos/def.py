import math


def atualiza_preco(n1):
    valor = round((n1 * 1.10),2)
    return valor


def taxa(n1):
    valor = round((atualiza_preco(n1) * (2.5/100)),2)
    return valor


def main():
    n1=float(input())
    print("%.2f" %atualiza_preco(n1))
    print("%.2f" % taxa(n1))

main()


