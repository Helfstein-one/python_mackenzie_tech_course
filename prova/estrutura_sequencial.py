peso=float(input())
altura=float(input())
imc = peso /(altura * altura)
if imc <16 or imc >40:
    print(imc)