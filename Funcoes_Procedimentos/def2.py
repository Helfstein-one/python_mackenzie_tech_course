def valorPagamento(valor, dias):
    if dias == 0:
        return valor
    else:
        a = valor * 0.03
        b = (((0.1/100) * dias)) * valor
        tot = valor + a + b
        return tot

def main():
    valor = str(input())
    valor = float(valor)
    dias = int(input())
    print(valorPagamento(valor, dias))

main()
