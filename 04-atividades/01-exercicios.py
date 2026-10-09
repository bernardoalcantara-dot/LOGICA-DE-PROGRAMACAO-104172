import os

soma = 0
quantidade_notas = 0

while True:
    os.system("cls")
    print('''
    === MENU ===
    S - inserir uma nota
    N - calcular media aritmetica
    ''')

    resposta = float(input("Deseja inderir uma nota? ")).lower()

    match respostas:
        case "s":
            nota = float(input("Digite uma nota: "))
            soma += nota
        case "n":
                break
            case_:
                print("Opção invalida! \n")
                input("Pressione uma tecla para continuar...")

if quantidade__notas == 0
    print("Não foram inseridas notas. \n")
    else:
        media = soma / quantidade_notas
        print(f"Média: {media}")