#bibliotecas
import os
import json

#lista
usuarios = []


# limpa terminal
os.system("cls" if os.name == "nt" else "clear")

#loop
while True:
    # menu
    print("1 - Cadastrar novo usuário")
    print("2 - Listar Usuários cadastrados")
    print("3 - Alterar dados do usuário")
    print("4 - Excluir usuário")
    print("5 - Graver usuários em JSON")
    print("6 - Abrir arquivo JSON")
    print("7 - Sair do programa")
    opcao = input("Opção desejada: ").strip()
    os.system("cls" if os.name == "nt" else "clear")
    match opcao:
        case "1":
            # inicializar um dicionário
            usuario = {}

            # informa os dados
            usuario['nome'] = input("Infome o nome:").strip().title()
            usuario['email'] = input("Infome o E-mail:").strip().lower()
            usuario['telefone'] = input("Infome o telefone:").strip()
            usuario['cpf'] = input("Infome o cpf:").strip()

            # Adicionar novo usuário na lista
            usuarios.append(usuario)
            os.system("cls" if os.name == "nt" else "clear")
            print(f"{usuario.get('nome')} cadastrado com sucesso.")

            continue

        case "2":
            # lista usuários cadastrados
            if usuarios:
                for i, usuario in enumerate(usuarios):
                    print(f"ID: {i}")
                    for chave, valor in usuario.items():
                        print(f"{chave.capitalize()}: {valor}.")
                    print(f"{'-'*25}")
            else:
                print("Não existe usuário cadastrado.")
            continue
        case "3":
            # Alterar dado do usuário
            try: # evitar que o sistema trave e volta novamente para as opções essa e a funçãp do try
                indice = int(input("Informe o ID do usuário a ser alterado: "))
                for chave, valor in usuarios[indice].items():
                    print(f"{chave.capitalize()}: {valor}.")
                chave = input("Qual chave deseja alterar o valor? ").strip().lower()
                usuarios[indice][chave] = input("Informe o novo valor: ").strip()
                os.system("cls" if os.name == "nt" else "clear")
                print(f"Dados de {usuarios[indice].get('nome')} alterado com sucesso!")
                continue
            except Exception as e:
                print(f"Não foi possivel atualizar os dados.  {e}.")
        case "4":
            try:
                indice = int(input("Informe o ID a ser excluido: "))
                del usuarios[indice]
                os.system("cls" if os.name == "nt" else "clear")
                print("Usuário excluido com sucesso!")
                continue
            except Exception as e:
                print(f"Não foi possível excluir. {e}.")
        case "5":
            arquivo = input("Informe o nome do arquivo: ").strip()
            with open(f"atv01_resolucao/{arquivo}.json","w",encoding="utf-8") as f: #cria o arquivo json
                json.dump(usuarios, f)  # dump e o comando de gravar
            os.system("cls" if os.name == "nt" else "clear")
            print("Dados gravados com sucesso!")
            continue
        case "6":
            try:
                arquivo = input("Informe o arquivo que deseja abrir: ").strip()
                with open(f"atv01_resolucao/{arquivo}.json","r",encoding="utf-8") as f:
                    usuarios = json.load(f)
                os.system("cls" if os.name == "nt" else "clear")
                print("Dados importados com sucesso!")
                continue
            except Exception as e:
                print(f"Não foi possível abrir o arquivo. {e}.")
        case "7":
            break
        case _:
            print("Opção inválida.")
            continue


