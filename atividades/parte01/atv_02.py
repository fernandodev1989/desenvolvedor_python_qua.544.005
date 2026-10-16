'''Crie um programa em que o usuário informe uma unica vez o nome e a idade, e em seguida o sistemaexibe ima lista de 5 filmes , suas salas e classificação indicativa.
O usuario deverá escolher a sala. Se tiver a idade indicativa o programa imprime o ingresso e encerra, Senão, o programa impede a entrada do usuário e retorna a lista para escolha de outro filme.
'''
nome = input(" Digite seu nome ").strip().title()
idade = int(input("Imfome sua idade!"))

filme1 = "Sala 01 - Rei leão"
filme2 = "Sala 02 - Ben 10"
filme3 = "Sala 03 - Thor"
filme4 = "Sala 04 - Titanic"
filme5 = "Sala 05 - A freira"

if idade < 12:
   print(f"{filme1} Classificação livre")
       
elif idade <= 12:
    print(f"Escolha entre{filme1},{filme2}")

elif idade <= 14:
    print(f"Escolha entre{filme1},{filme2},{filme3}")

elif idade <= 16:
    print(f"Escolha entre {filme1},{filme2},{filme3},{filme4}")

else:
    print(f"Escolha entre{filme1},{filme2},{filme3},{filme4},{filme5}")

