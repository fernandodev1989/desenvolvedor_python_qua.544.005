#Biblioteca 
import os


# funções
def limpar():
    os.system("cls" if os.name == "nt" else "clear") 

def boas_vindas(nome):
    return f"{nome}, seja bem vindo!"


# Algoritimo principal
limpar()
nome = input("Informe seu nome: ").strip().title()
print(boas_vindas(nome),(nome))