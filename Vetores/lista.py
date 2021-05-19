listaCarro = []
listaConsumo = []

while len(listaCarro) < 5:
    listaCarro.append(input())
    listaConsumo.append(float(input()))
    print('\n')

results = ''
valor_gas = 2.25
total_km = 1000
for j, c in enumerate(listaCarro):
    consumo_l = round(total_km/listaConsumo[j], 2)
    results += 'O carro {} consume {}L e custará $R{} quando fizer {}km\n'.format(c, consumo_l, round(consumo_l*valor_gas, 2), total_km)
print('O carro mais económico é o {}'.format(listaCarro[listaConsumo.index(max(listaConsumo))]))
