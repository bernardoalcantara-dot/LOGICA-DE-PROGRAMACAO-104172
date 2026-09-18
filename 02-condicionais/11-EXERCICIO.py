import os
os.system("cls")

#ENTRADA.
sexo = input("digite o sexo (M/F): ")
altura = float(input("digite a altura em metros: "))

if  sexo == "M":
   peso = (72.7 * altura) - 58
   print("O peso ideal é:", peso, "KG")

elif sexo == "F":
    peso =(62.1 * altura) - 44.7
    print("o peso ideal é", peso,"kg")

else:
    print("sexo invalido")