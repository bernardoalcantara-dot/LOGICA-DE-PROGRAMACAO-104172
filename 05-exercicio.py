import os
os.system('cls')

#ENTRADA.
numero1 = int(input("digite um numero: "))
numero2 = int(input("digite outro numero: "))
operacao = str(input("digite um caractere: "))

#PROCESSAMENTO.
match operacao:
    case "*":
        resultado = numero1*numero2
    case "+":
        resultado = numero1 + numero2
    case "-":
        resultado = numero1 + numero2
    case "-":
        resultado = numero1 - numero2
    case _:
        resultado = "operacao invalida"

#SAIDA.
print("resultado:", resultado)