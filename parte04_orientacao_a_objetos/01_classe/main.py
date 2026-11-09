# POO - 1° Criar uma classe - atributos ex: nome, cpf - classe sempre se inicia com letra maiuscula
#Classe
class Pessoa:
    # Construtor da classe - 
    def __init__(self,nome,idade,email,cpf):
        #atributos
        self.nome = nome
        self.idade = idade
        self.email = email
        self.cpf = cpf

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"E_mail: {self.email}")
        print(f"CPF: {self.cpf}")

#Algoritmo Principal obs: Fora da classe. Criar o objeto

def main():
    # Instanciar a classe
    usuario = Pessoa(nome="",idade=0,email="",cpf="")

    #insere valores nos atributos
    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.idade = input("Informe o idade: ")
    usuario.email = input("Informe o e-mail: ").strip().lower()
    usuario.cpf = input("Informe o cpf: ").strip()

    # exibe os atributos na tela
    usuario.exibir_dados()

if __name__ == "__main__":
    main()