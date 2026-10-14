import os
os.system("cls")

print("= INSERINDO NÙMEROS NO VETOR =")
vetor_numeros = []

for i in range(3):
    numero = int(input("Digite um número: "))
    vetor_numeros.append(numero)
    
    print("\n= EXIBINDO NÙMEROS DO VETOR =")
    for valor in vetor_numeros: # ForEach
        print(f"Valor: {valor}")
        
        