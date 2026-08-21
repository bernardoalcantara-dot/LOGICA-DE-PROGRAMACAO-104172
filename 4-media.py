import os

# Limpa o terminal
os.system('cls')

print('= SOLICITANDO DADOS =')
nome = input('digite seu nome: ')
idade = int(input('digite sua idade: '))
primeira_nota = float(input('primeira nota: '))
segunda_nota = float(input('digite a segunda nota: '))

media =(primeira_nota + segunda_nota) / 2

print ('\n= EXIBINDO DADOS =')
print('nome: ', nome)
print('idade: ', idade)
print('primeira nota: ', primeira_nota)
print('segunda nota: ', segunda_nota)
print('media: ', media)