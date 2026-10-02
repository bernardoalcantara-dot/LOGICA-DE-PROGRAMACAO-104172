import os
os.system("cls")


nota1 = float(input("Digite a primeira nota: "))
while nota1 < 0 or nota1 > 10:
    nota1 = float(input("Nota inválida! Digite novamente: "))

nota2 = float(input("Digite a segunda nota: "))
while nota2 < 0 or nota2 > 10:
    nota2 = float(input("Nota inválida! Digite novamente: "))

nota3 = float(input("Digite a terceira nota: "))
while nota3 < 0 or nota3 > 10:
    nota3 = float(input("Nota inválida! Digite novamente: "))

media = (nota1 + nota2 + nota3) / 3

print("Média:", media)

if media >= 7:
    print("Aluno aprovado!")
elif media >= 5:
    print("Aluno em recuperação!")
else:
    print("Aluno reprovado!")