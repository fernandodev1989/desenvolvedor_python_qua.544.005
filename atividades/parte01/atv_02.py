'''Crie um programa em que o usuário informe uma unica vez o nome e a idade, e em seguida o sistemaexibe ima lista de 5 filmes , suas salas e classificação indicativa.
O usuario deverá escolher a sala. Se tiver a idade indicativa o programa imprime o ingresso e encerra, Senão, o programa impede a entrada do usuário e retorna a lista para escolha de outro filme.'''
# import a biblioteca
import os

# Limpa o terminal
os.system("cls" if os.name == "nt" else "clear")

nome = input(" Digite seu nome ").strip().title()
idade = int(input("Imfome sua idade!"))
idade_minima = None 

#loop
while True:

    print("----- CINEMA -----")
    print("01 - Rei leão - livre")
    print("02 - Tarzan - 10 anos")
    print("03 - Batman - 14 anos")
    print("04 - Titanic - 16 anos")
    print("05 - A freira - 18 anos")

    # usuário informa a sala - .strip ignora o espaço teclado pelo cliente
    sala = input("Escolha o filme ").strip()

    # Atribui a idade minima do filme
    match sala:
        case "1":
            idade_minima = 0
        case "2":
            idade_minima = 10 
        case "3":
            idade_minima = 14
        case "4":
            idade_minima = 16 
        case "5":
            idade_minima = 18 
        case _:
            print("Sala inexistente.")
            idade_minima = idade + 1

    if idade >= idade_minima:
        print(f"Ingresso impresso para {nome}")
        print("Tenha um bom filme!")
        break
    else:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"Ingresso negado para{nome}")
        print("Você não possui idade para ver o filme")
        print("Escolha outro filme")
        continue
 