import os

from model import Pessoa,Endereco


def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    endereco = Endereco(cep="",uf="",cidade="",bairro="",logradouro="",complemento="",numero="")
    usuario = Pessoa(nome="",cpf="",email="",telefone="",endereco=endereco)

    limpar()

    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.cpf = input("Informe o cpf: ").strip()
    usuario.email = input("Informe o email: ").strip().lower()
    usuario.telefone = input("Informe o telefone: ").strip()
    usuario.cep = input("Informe o cep: ").strip()
    usuario.uf = input("Informe o uf: ").strip().upper()
    usuario.cidade = input("Informe a cidade: ").strip().title()
    usuario.bairro = input("Informe o bairro: ").strip().title()
    usuario.logradouro = input("Informe o logradouro: ").strip()
    usuario.complemento = input("Informe o complemento: ")
    usuario.numero = input("Informe o número: ").strip()

    #saida de dados
    usuario.exibir_dados()


if __name__ == "__main__":
    main()