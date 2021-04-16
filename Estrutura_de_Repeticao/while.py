numero_de_notas=int(input())
if numero_de_notas==0:
    print("NÃO HOUVE PROCESSAMENTO")
else:
    cont=0
    total_notas=0
    while cont<numero_de_notas:
        nota = float(input())
        total_notas += nota
        cont= cont + 1
        if nota>=6.0:
            print("PARABÉNS VOCÊ ESTÁ APROVADO")
    print((float(total_notas/numero_de_notas)))













