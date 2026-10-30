import os
os.system("cls")

pacientes = []

def cadastrar_paciente():
    nome = input("Nome: ").strip()
    sobrenome = input("Sobrenome: ").strip()

    if nome == "" or sobrenome == "":
        print("Nome e sobrenome não podem ficar em branco!")
        return

    paciente = {
        "nome": nome,
        "sobrenome": sobrenome
    }

    pacientes.append(paciente)
    print("Paciente cadastrado com sucesso!")

def listar_pacientes():
    if len(pacientes) == 0:
        print("Nenhum paciente cadastrado.")
        return

    print("\n--- LISTA DE PACIENTES ---")

    for i, paciente in enumerate(pacientes):
        print(f"{i + 1}. {paciente['nome']} {paciente['sobrenome']}")

def atualizar_paciente():
    listar_pacientes()

    if len(pacientes) == 0:
        return

    try:
        numero = int(input("Número do paciente: "))

        if numero < 1 or numero > len(pacientes):
            print("Paciente inexistente!")
            return

        nome = input("Novo nome: ").strip()
        sobrenome = input("Novo sobrenome: ").strip()

        if nome == "" or sobrenome == "":
            print("Nome e sobrenome não podem ficar em branco!")
            return

        pacientes[numero - 1]["nome"] = nome
        pacientes[numero - 1]["sobrenome"] = sobrenome

        print("Paciente atualizado com sucesso!")

    except ValueError:
        print("Digite um número válido!")

def excluir_paciente():
    listar_pacientes()

    if len(pacientes) == 0:
        return

    try:
        numero = int(input("Número do paciente que deseja excluir: "))

        if numero < 1 or numero > len(pacientes):
            print("Paciente inexistente!")
            return

        paciente = pacientes.pop(numero - 1)

        print(f"Paciente {paciente['nome']} {paciente['sobrenome']} excluído!")

    except ValueError:
        print("Digite um número válido!")

def buscar_paciente():
    busca = input("Digite o nome ou sobrenome: ").strip().lower()

    if busca == "":
        print("A busca não pode ficar em branco!")
        return

    encontrados = []

    for paciente in pacientes:
        nome_completo = paciente["nome"] + " " + paciente["sobrenome"]

        if busca in nome_completo.lower():
            encontrados.append(paciente)

    if len(encontrados) == 0:
        print("Nenhum paciente encontrado.")
    else:
        print("\n--- PACIENTES ENCONTRADOS ---")

        for i, paciente in enumerate(encontrados):
            print(f"{i + 1}. {paciente['nome']} {paciente['sobrenome']}")

def menu():
    while True:
        print("\n===== CADASTRO DE PACIENTES =====")
        print("1. Cadastrar paciente")
        print("2. Listar pacientes")
        print("3. Atualizar paciente")
        print("4. Excluir paciente")
        print("5. Buscar paciente")
        print("0. Sair")

        opcao = input("\nOpção: ")

        if opcao == "1":
            cadastrar_paciente()

        elif opcao == "2":
            listar_pacientes()

        elif opcao == "3":
            atualizar_paciente()

        elif opcao == "4":
            excluir_paciente()

        elif opcao == "5":
            buscar_paciente()

        elif opcao == "0":
            print("Programa encerrado!")
            break

        else:
            print("Opção inválida! Tente novamente.")

menu()