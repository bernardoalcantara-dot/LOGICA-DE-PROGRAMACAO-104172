import os
import time

while True:
    os.system("cls")
    print('''
=== MENU ===
1 - Adicionar uma pessoa
2 - Exibir resultados
3 - Sair
''')
    opção = int(input("Digite a opção desejada: "))

    match opção:
        case 1:
            print("===  CADASTRO ===")
        idade = int(input("Digite sua idade; "))
        sexo = input("digite o sexo (M/F:):").upper()salario = float(input('Digite o salário: R$ '))

            soma_salario += salario
            contador_pessoas += 1
            maior_idade = max(idade, maior_idade)
            menor_idade = min(idade, menor_idade)

            if sexo == 'F' and salario >= 5000:
                mulheres_5K += 1

            print('Pessoa adicionada com sucesso!')
            input('Pressione uma tecla para continuar...')
        case 2:
            if contador_pessoas == 0:
                print('\nNenhuma pessoas cadastrada. \n')
                input('Pressione uma tecla para continuar...')
            else:
                media_salario = soma_salario / contador_pessoas

                print('\n=== RESULTADOS DA PESQUISA ===')
                print(f'Média de salário do grupo: R$ {media_salario}')
                print(f'Maior idade: {maior_idade}')
                print(f'Menor idade: {menor_idade}')
                print(f'Mulheres com salário a partir de R$ 5.000,00: {mulheres_5K}')
                input('Pressione uma tecla para continuar...')
        case 3:
            print('\nEncerrando o programa.')
            break
        case _:
            print('\nOpção inválida! \n')
            input('Pressione uma tecla para continuar...'