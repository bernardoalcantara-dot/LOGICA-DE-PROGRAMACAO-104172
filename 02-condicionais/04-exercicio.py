import os
os.system

# ENTRADA
dia = int(input("Digite o número do dia da semana (1 a 7): "))

# PROCESSAMENTO
if dia == 1 or dia == 7:
    resultado = "Final de semana"
elif dia >= 2 and dia <= 6:
    resultado = "Dia útil"
else:
    resultado = "Inválido"

# SAÍDA
print(resultado)