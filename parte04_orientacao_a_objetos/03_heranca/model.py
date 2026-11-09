'''  4 pilares da orientação a objetos
- herança, polimorfismo, abstração e encapsulamento
'''
# Herança = generalização - evitar redundância 

# superclasse / classe pai
class Pessoa:
    def __init__(self, email, telefone, endereco):
        self.email = email
        self.telefone = telefone
        self.endereco = endereco

# metodo de classes
    def exibir_dados(self):
        print(f"E-mail: {self.email}")
        print(f"Telefone: {self.telefone}")
        print(f"Endereço: {self.endereco}")


# Subclasses / classes-filhas
class PessoaFisica(Pessoa):
    def __init__(self,nome,cpf,email,telefone,endereco):
        self.nome = nome
        self.cpf = cpf
        super().__init__(email=email,telefone=telefone,endereco=endereco)

    def exibir_dados(self):
        print(f"{'-'*20} DADOS DO USUÁRIO {'-'*20}")
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        super().exibir_dados()


class PessoaJuridica(Pessoa):
    def __init__(self,cnpj,razao_social,nome_fantasia,email,telefone,endereco):
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
        super().__init__(email=email,telefone=telefone,endereco=endereco)

    def exibir_dados(self):
        print(f"{'-'*20} DADOS DO USUÁRIO {'-'*20}")
        print(f"Razão social: {self.razao_social}")
        print(f"Nome da empresa: {self.nome_fantasia}")
        print(f"CNPJ: {self.cnpj}")
        super().exibir_dados()