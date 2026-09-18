import os
os.system("cls")

#ENTRADA.
picanha = 1
lasanha = 2
strogonoff = 3
bife_acebolado = 4
pao_com_ovo = 5
pedido = int(input("digite o codigo do seu pedido"))

#MENU.
print("""
=== MENU ===
1 - PICANHA
2 - LASANHA
3 - STROGONOFF
4 - BIFE ACEBOLADO
5 - PAO COM OVO
""")

#PROCESSAMENTO.
match pedido:
    case 1:
        prato = "picanha"
        valor = 25
    case 2:
        prato = "lasanha"
        valor = 20
    case 3:
        prato ="strogonoff"
        valor = 18
    case 4:
        prato = "bife acebolado"
        valor = 15
    case 5:
        prato = "pao com ovo"
        valor = 10