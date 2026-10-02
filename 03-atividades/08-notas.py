import os
os.system("cls")

print("=== SOLICITANDO DADOS ===")

QUANTIDADE_NOTAS = 3
soma_notas = 0.0

for i in range(QUANTIDADE_NOTAS):
    soma_notas += float(input("Digite a nota:"))
    media = soma_notas / QUANTIDADE_NOTAS
if  media >= 7.0:
    print("APROVADO.")

else:
    print("REPROVADO.")

print(f"A média do aluno foi: {media}")