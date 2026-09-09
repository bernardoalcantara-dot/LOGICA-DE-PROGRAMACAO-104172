import os
os.system("cls")

#ENTRADA.
idade = int(input("digite sua idade: "))
sexo = input("digite o sexo (M ou F): ")

#PROCESSAMENTO.
if idade >= 18 and sexo == "M":
    resultado = "deve apresentar-se ao serviço militar." 
else:
    resultado = "nao deve apresentar-se ao serviço militar"

#SAIDA.
print(f"resultado: {resultado}")