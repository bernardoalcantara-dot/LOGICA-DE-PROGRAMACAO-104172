import os
os.system("cls")

#ENTRADA.
mes = int(input("digite o numero do mes (1 a 12): "))

#PROCESSAMENTO.
match mes:
    case 1:
        nome_mes = "janeiro"
    case 2:
        nome_mes = "fevereiro"
    case 3:
        nome_mes = "marco"
    case 4:
        nome_mes = "abril"
    case 5:
        nome_mes = "maio"
    case 6:
        nome_mes = "junho"
    case 7:
        nome_mes = "julho"
    case 8:
        nome_mes = "agosto"
    case 9:
        nome_mes = "setembro"
    case 10:
        nome_mes = "outubro"
    case 11:
        nome_mes = "novembro"
    case 12:
        nome_mes = "dezembro"
    case _:
        nome_mes = "mes invalido"

#SAIDA.
print(nome_mes)