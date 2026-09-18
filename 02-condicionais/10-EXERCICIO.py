import os
os.system("cls")

#ENTRADA.
valor = float(input("digite o valor do produto: "))
print("1 - pagamento á vista")
print("2 - pagamento á prazo")

#PROCESSAMENTO.
match "forma":

    case 1:
        desconto = valor * 0.10
        total = valor - desconto

        #SAIDA.
        print("\nValor do produto: RS", valor)
        print("Forma de pagamento: a prazo")
        print("Quantidade de parcelas:", "parcela")
        print("Valor por parcelas: RS", "valor_parcela")
        print("Total a prazo: RS", "valor")
    case _:
        print("forma de pagamento invalida")