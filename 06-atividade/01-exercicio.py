import os
os.system("cls")

vetor_numeros = []
soma_positivos = 0
quantidade_impares = 0
QUANTIDADE = 5

print("= SOLICITANDO DADOS =")
for i in range(QUANTIDADE)
    numero = int(input(f"Digite o {i+1} número: "))
    
    if numero < 0:
        numero = 0
        
        vetor_numeros.append(número)
        
        print("\n= EXIBINDO DADOS =")
        for posicao, numero in enumerate(vetor_numeros, start=1):
            print(f"{posicao} {numero}")