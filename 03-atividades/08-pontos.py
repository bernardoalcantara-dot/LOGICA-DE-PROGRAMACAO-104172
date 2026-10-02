import os
os.system("cls")
soma = 0
QUANTIDADE NOTAS = 2

for i in range(QUANTIDADE_NOTAS):
    while True:
        nota = float(input(f"Digite a {i+1}" nota do aluno entre 0 a 10: "))
        if nota >= 0 and nota <= 10:
                print("nota invalida! \n Tente novamente! \n")
                input("Pressione uma tecla!...")
                os.system("cls")
        else:
            print("nota valida!")
            soma = soma + nota
            break
        else:
            

