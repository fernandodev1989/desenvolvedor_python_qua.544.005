#TODO: parte 03 atividade 01
'''
Crie um programa que calcule o peso de uma pessoa em um planeta do sistema solar escolhida por ela.
'''
# NOTE: Pesquisa pela aceleração da gravidade em cada planeta.
# NOTE: Inclua a lua na lista de planetas


import modulo

modulo.limpar()
print(f"{'-'*20} Escolha um planeta {'-'*20}")
print("1 - Sol")
print("2 - Jupiter")
print("3 - Notuno")
print("4 - Saturno")
print("5 - Terra")
print("6 - Venus")
print("7 - Urano")
print("8 - Marte")
print("9 - Mercurio")
print("10 - Lua")
print("11 - Plutao (planeta anao)")



while True:
    massa = float(input("Informe sua massa na terra").replace(",","."))
