import os

from model import Pessoa


def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    usuario = Pessoa(nome="",cpf="",email="",idade=0,altura=0.0)

    limpar()
    usuario.nome = input("Inforne o nome: ").strip().title()
    usuario.cpf = input("Inforne o cpf: ").strip()
    usuario.email = input("Inforne o email: ").strip().lower()
    usuario.idade = input("Inforne a idade: ")
    usuario.altura = input("Inforne a altura: ").replace(",",".")

    limpar()
    print(f"Nome: {usuario.nome}")
    print(f"CPF: {usuario.cpf}")
    print(f"Email: {usuario.email}")
    print(f"Idade: {usuario.idade}")
    print(f"Altura: {usuario.altura}")


if __name__ == "__main__":
        main()



