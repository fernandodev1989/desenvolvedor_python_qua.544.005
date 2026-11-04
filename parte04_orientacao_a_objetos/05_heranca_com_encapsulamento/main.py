import os

from model import PessoaFisica,PessoaJuridica


def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    # instanciando as classes
    usuario = PessoaFisica(nome="",cpf="",email="",telefone="")
    empresa = PessoaJuridica(razao_social="",nome_fantasia="",cnpj="",email="",telefone="")

    limpar()
    print(f"{'-'*20} Informe o nome do usuário {'-'*20}")
    usuario.nome = input("informe o nome: ").strip().title()
    usuario.cpf = input("informe o cpf: ").strip()
    usuario.email = input("informe o email: ").strip().lower()
    usuario.telefone = input("informe o telefone: ").strip()

    limpar()
    print(f"{'-'*20} Informe os dados da empresa  {'-'*20}")
    empresa.razao_social = input("informe a razao social: ").strip()
    empresa.nome_fantasia = input("informe o nome: ").strip()
    empresa.cnpj = input("informe o cnpj: ").strip()
    empresa.email = input("informe o email: ").strip().lower()
    empresa.telefone = input("informe o telefone: ").strip()

    limpar()
    print(f"{'-'*20} DADOS DO USUÁRIO {'-'*20}")
    print(f"Nome: {usuario.nome}")
    print(f"Cpf: {usuario.cpf}")
    print(f"Email: {usuario.email}")
    print(f"Telefone: {usuario.telefone}")
    print(f"{'-'*20} DADOS DA EMPRESA {'-'*20}")
    print(f"Razao social: {empresa.razao_social}")
    print(f"Nome fantasia: {empresa.nome_fantasia}")
    print(f"CNPJ: {empresa.cnpj}")
    print(f"email: {empresa.email}")
    print(f"telefone: {empresa.telefone}")


if __name__ == "__main__":
    main()
