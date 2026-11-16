import os
os.system("cls")

def calcular_notas(list_notas):
    return sum(lista_notas) / len(lista_notas)

lista_notas = []

for i in range(3):
    nota = float(input("Digite uma nota: "))
    lista_notas.append(nota)
    
    media = calcular_notas(lista_notas)
    
    print(f"Média: {media}")