import os
os.system("cls")

#ENTRADA.
dia = int(input("digite um numero de 1 a 7: "))

#PROCESSAMENTO E SAIDA.
if dia == 1 or dia == 7:
    print("final de semana")
elif dia >= 2 and dia <= 6:
    print("dia util")
else:
    print("invalido")