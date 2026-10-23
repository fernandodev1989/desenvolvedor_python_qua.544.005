
# parte 02 atividade 01
'''
Crie um programa que faça as seguintes operações:
- Cadastra novo usuário (nome, email, telefone, cpf).
- lista todos os usuarios cadastrados.
- Altera os dados de um usuário.
- Exclui um usuário.
- Grava os dados de todos os usuários em um .json.
- Abre arquivo .json e lista todos os usuários cadastrados nele.
'''

import json
import os

usuarios = []


os.system ("cls" if os.name == "nt" else "clear")


while True:
    print("1 - cadastrar novo usuário")
    print("2 - Mostrar usuários cadastrados")
    print("3 - Alterar dados do usuário")
    print("4 - Excluir usuário")
    print("5 - Gravar dados de todos os usuarios em .json ")
    print("6 - Abrir arquivo .jason e mostrar usuários cadastrados")
    opcao = input("Opção desejada: ").strip()
    os.system ("cls" if os.name == "nt" else "clear")
    match opcao:
        case "1":
            usuario = {}
            usuario["nome"] = input("Informe o nome: ").strip().title()
            usuario["telefone"] = input("Informe o telefone: ").strip()
            usuario["email"] = input("Informe o email: ").strip().lower()
            usuario["cpf"] = input("Informe o CPF: ").strip()

            usuarios.append(usuario)
            os.system("cls" if os.name == "nt" else "clear")
            print(f"{usuario.get('nome')} cadastrado com sucesso!")
            continue

           
        case "2":  
            for usuario in usuarios:
                for chave, valor in usuario.items():
                    print(f"{chave.capitalize()}: {valor}")