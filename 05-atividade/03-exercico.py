import os
os.system("cls")

nomes = []

for i in range (5):
    livros = input("Escreva o nome do livro: ")
    nomes.append(livros)
    
    for i in range (5):
        print(f"livros: {nomes}")