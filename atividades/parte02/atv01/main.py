
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

os.system("cls" if os.name == "nt" else "clear")

while True:
    print("\n--- SISTEMA DE GESTÃO DE UTILIZADORES ---")
    print("1 - Cadastrar novo usuário")
    print("2 - Mostrar usuários cadastrados")
    print("3 - Alterar dados do usuário")
    print("4 - Excluir usuário")
    print("5 - Gravar dados de todos os usuários em .json")
    print("6 - Abrir arquivo .json e mostrar usuários cadastrados")
    print("0 - Sair")
    
    opcao = input("Opção desejada: ").strip()
    os.system("cls" if os.name == "nt" else "clear")
    
    match opcao:
        case "1":
            usuario = {}
            usuario["nome"] = input("Informe o nome: ").strip().title()
            usuario["telefone"] = input("Informe o telefone: ").strip()
            usuario["email"] = input("Informe o email: ").strip().lower()
            usuario["cpf"] = input("Informe o CPF: ").strip()

            usuarios.append(usuario)
            os.system("cls" if os.name == "nt" else "clear")
            print(f" {usuario.get('nome')} cadastrado com sucesso!")
            input("\nPressione Enter para continuar...")
            os.system("cls" if os.name == "nt" else "clear")

        case "2":  
            if not usuarios:
                print("\n Nenhum usuário cadastrado ainda.")
            else:
                print("\n--- LISTA DE UTILIZADORES ---")
                for indice, usuario in enumerate(usuarios):
                    print(f"\n[{indice + 1}] Utilizador:")
                    print(f"  Nome:     {usuario['nome']}")
                    print(f"  Telefone: {usuario['telefone']}")
                    print(f"  E-mail:   {usuario['email']}")
                    print(f"  CPF:      {usuario['cpf']}")
                print("-" * 25)
            input("\nPressione Enter para continuar...")
            os.system("cls" if os.name == "nt" else "clear")

        case "3":
            if not usuarios:
                print("\n Nenhum usuário cadastrado ainda.")
            else:
                print("\n--- ALTERAR DADOS DE UTILIZADOR ---")
                for indice, usuario in enumerate(usuarios):
                    print(f"[{indice + 1}] Nome: {usuario['nome']} | CPF: {usuario['cpf']}")
                print("-" * 25)
                
                try:
                    escolha = int(input("\nInforme o número do usuário que deseja alterar: ")) - 1
                    
                    if 0 <= escolha < len(usuarios):
                        u = usuarios[escolha]
                        print(f"\nEditando dados de: {u['nome']}")
                        print("*(Pressione Enter sem digitar nada para manter o dado atual)*\n")
                        
                        novo_nome = input(f"Novo nome [{u['nome']}]: ").strip()
                        novo_tel = input(f"Novo telefone [{u['telefone']}]: ").strip()
                        novo_email = input(f"Novo email [{u['email']}]: ").strip()
                        novo_cpf = input(f"Novo CPF [{u['cpf']}]: ").strip()
                        
                        if novo_nome:
                            u['nome'] = novo_nome.title()
                        if novo_tel:
                            u['telefone'] = novo_tel
                        if novo_email:
                            u['email'] = novo_email.lower()
                        if novo_cpf:
                            u['cpf'] = novo_cpf
                            
                        os.system("cls" if os.name == "nt" else "clear")
                        print(" Dados alterados com sucesso!")
                    else:
                        print(" Número inválido!")
                except ValueError:
                    print(" Por favor, digite apenas números inteiros válidos.")
                    
            input("\nPressione Enter para continuar...")
            os.system("cls" if os.name == "nt" else "clear")

        case "4":
            if not usuarios:
                print("\n Nenhum usuário cadastrado ainda para excluir.")
            else:
                print("\n--- EXCLUIR UTILIZADOR ---")
                for indice, usuario in enumerate(usuarios):
                    print(f"[{indice + 1}] Nome: {usuario['nome']} | CPF: {usuario['cpf']}")
                print("-" * 25)
                
                try:
                    escolha = int(input("\nInforme o número do usuário que deseja excluir: ")) - 1
                    
                    if 0 <= escolha < len(usuarios):
                        usuario_removido = usuarios.pop(escolha)
                        os.system("cls" if os.name == "nt" else "clear")
                        print(f" Utilizador '{usuario_removido['nome']}' excluído com sucesso!")
                    else:
                        print(" Número inválido!")
                except ValueError:
                    print(" Por favor, digite apenas números inteiros válidos.")
                    
            input("\nPressione Enter para continuar...")
            os.system("cls" if os.name == "nt" else "clear")

        case "5":
            try:
                with open("usuarios.json", "w", encoding="utf-8") as arquivo:
                    json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)
                print("\n Dados gravados com sucesso no arquivo 'usuarios.json'!")
            except Exception as e:
                print(f"\n Erro ao gravar o arquivo: {e}")
                
            input("\nPressione Enter para continuar...")
            os.system("cls" if os.name == "nt" else "clear")

        case "6":
            try:
                with open("usuarios.json", "r", encoding="utf-8") as arquivo:
                    usuarios_do_arquivo = json.load(arquivo)
                
                if not usuarios_do_arquivo:
                    print("\n O arquivo JSON está vazio.")
                else:
                    print("\n--- UTILIZADORES LIDOS DO ARQUIVO JSON ---")
                    for indice, usuario in enumerate(usuarios_do_arquivo):
                        print(f"[{indice + 1}] Nome: {usuario['nome']} | E-mail: {usuario['email']} | CPF: {usuario['cpf']}")
                    print("-" * 25)
            except FileNotFoundError:
                print("\n Nenhum arquivo 'usuarios.json' encontrado. Grave os dados primeiro (Opção 5).")
            except Exception as e:
                print(f"\n Erro ao ler o arquivo: {e}")
                
            input("\nPressione Enter para continuar...")
            os.system("cls" if os.name == "nt" else "clear")

        case "0":
            print("\n A sair do programa. Até logo!")
            break

        case _:
            print("\n Opção inválida! Escolha uma opção entre 0 e 6.")
            input("\nPressione Enter para continuar...")
            os.system("cls" if os.name == "nt" else "clear")