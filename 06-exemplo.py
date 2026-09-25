import os
os.system("cls")
#Constante.
QUANTIDADEREPETICOES = 5
pares = 0
impares = 0

for i in range(QUANTIDADEREPETICOES):
    numero = int(input("\nDigite um numero:"))
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
        print(f"\nQuantidade de numeros PARES: {pares}")
        print(f"Quantidade de numeros IMPARES: {impares}")