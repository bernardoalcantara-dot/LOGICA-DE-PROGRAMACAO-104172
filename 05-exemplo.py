import os
os.system("cls")

print("ACUMULANDO VALORES EM UMA VARIAVEL.")
soma = 0

print(f"valor INICIAL da variavel soma: {soma}")

for i in range(3):
    numero = int(input("\nDigite um numero para somar: "))
    soma = soma + numero
    print(f"Valor TEMPORARIO da variavel soma: {soma}")

print(f"\nValor FINAL da variavel soma: {soma}")