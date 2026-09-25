import os
os.system("cls")

nota = 0
materias = 4

for P in range(materias):
    nota = float(input("Digite sua nota:"))

media=nota/materias

print("sua media foi {media}.")