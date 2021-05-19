listaCarro = []
listaConsumo = []

def entrada_carro():
    listaCarro.append(input())
    listaCarro.append(input())
    listaCarro.append(input())
    listaCarro.append(input())

def entrada_consumo():
    listaConsumo.append(int(input()))
    listaConsumo.append(int(input()))
    listaConsumo.append(int(input()))
    listaConsumo.append(int(input()))

def economico():
    results = ''
    valor_gas = 2
    total_km = 1000
    for j, c in enumerate(listaCarro):
        consumo_l = round(total_km / listaConsumo[j], 2)
        results += '\n'.format(c, consumo_l, round(consumo_l * valor_gas, 2), total_km)
    return ''.format(listaCarro[listaConsumo.index(min(listaConsumo))])

def main():
    entrada_carro()
    entrada_consumo()
    print(economico())

main()