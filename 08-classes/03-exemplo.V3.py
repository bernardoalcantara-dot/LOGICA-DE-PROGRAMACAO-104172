from dataclasses import dataclass
import os
os.system("cls")

# CRIE UMA CLASSE PARA OS DADOS DE UM CLIENTE.
#DADOS: NOME, TELEFONE E EMAIL
@dataclass
class Cliente:
    nome: str
    telefone: str
    email: str
    
    lista_clientes = []
    
    print("= SOLICITANDO DADOS =")
    for i in range(2) 
    dados = Cliente(
        nome = input("Digite seu nome: ")
        telefone = input("Digite sua idade: "),
        email = ("Digite seu e-mail: ")
    )
    lista_clientes.append(dados)
    
    PRINT("\N= exibindo dados =")
    for clientes in lista_clientes:
        print(f"Nome: {cliente.nome}")
        print(f"telefone: {cliente.telefone}")
        print(f"E-mail: {cliente.email}")
        print("="*30)