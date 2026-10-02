import os
os.system("cls")

print("TELA PARA CADASTRO =")
login_cadastrado = ("Digite seu login: ")
senha_cadastrada = ("Digite sua senha: ")

while True:
    os.system("cls")
    print("= TELA PARA LOGIN =")
    login_informado = input("Digite seu login: ")
    senha_informada = input("Digite sua senha: ")

    login_correto = login_informado == login_cadastrado
    senha_correta = senha_informada == senha_cadastrada

    if login_correto and senha_correta:
        print("Bem vindo!")
        break
    else:
        print("Login ou senha incorretas. \nTente novamente!")
        input("Pressione uma tecla para continuar...")