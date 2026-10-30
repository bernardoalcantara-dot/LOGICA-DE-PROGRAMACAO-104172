import os

#lista de produtos.
lista_produtos= []

while True:
    #limpa o terminal.
    os.system("cls")

    #menu do programa.
    ('''
    === MERCADINHO DENDEZEIROS ===
    1-Cadastrar produtos
    2-Listar produtos
    0-Sair
    ''')

    opçao = int(input("Escolha uma opção: "))

    match opçao:
        case 1:
            #CREATE (INSERIR)
            print("\n== CADASTRAR PRODUTO ==")
            nome_produto = input ("Digite o nome do novo produto: ").strip().upper()
            if nome_produto in lista_produtos:
                print("Produto ja cadastrado.")
            else:
                lista_produtos.append(nome_produto)
                print("Produto cadastrado com sucesso!")
        case 2:
            # READ (LER / CONSULTAR/ BUSCAR)
            print("\n== PRODUTOS NO ESTOQUE ==")
            for produtos in lista_produtos:
                print(f"-{produtoS}")
            print(f"Total: {len(lista_produtos)}")
        case 3:
            # UPDATE (ATUALIZAR)
            print("\n== ATUALIZAR PRODUTO ==")
            nome = input("Qual produto deseja atualizar? ")
            if nome in lista_produtos:
                posicao = lista_produtos.index(nome)
                novo = input("Novo nome: ")
                lista_produtos[posicao] = novo
                print("Produto alterado com sucesso! ")
            else:
                print("Produto não encontrado.")
        case 4:
            # DELETE (EXCLUIR)
            print("\n== REMOVER PRODUTO ==")
            nome = input("Qual produto deseja remover? ")
            if nome in lista_produtos:
                lista_produtos.remove(nome)
                print("Produto excluido com sucesso!")
            else:
                print("Produto não encontrado.")
        case 5:
            print("\n== ENCONTRAR PRODUTO ==")
            nome = input("Qual produto deseja buscar? ")
            if nome in lista_produtos:
                print("Produto encontrado!")
            else:
                print("Este produto não esta no estoque")
            
        case 0:
            print("Saindo do programa...")
            break
        case _:
            print("Opção invalida! \nTente novamente...")
            
            input("Pressione uma tecla para continuar...")