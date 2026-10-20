# ALTERAR ITENS DA LISTA
# bibliotecas
import os

# lista
nomes = ["Fernando", "Julia", "Livia", "José", "Nayelle", "Maria", "Jackson", "Whinderson", "Clovis"]

os.system("cls" if os.name == "nt" else "clear")



# loop
while True:
    # exibe a lista original
    for n, nome in enumerate(nomes):
        print(f"Indice {n}: {nome}")
    #menu
    print("1 - Alterar item da lista")
    print("2 - Finalizar")
    opcao = input("Opção desejada: ").strip() #informa a opção desejada

    # verifica a opção desejada escolhida
    match opcao:
        case "1":
            #informa o itém a ser alterado
            indice = int(input("Informe o indice a ser alterado: "))
            #informa novo valor
            nomes[indice] = input("informe novo nome: ").strip().title()
            os.system("cles" if os.name == "nt" else "clear")
            print("Item da lista alterado com sucesso!")
            continue

        case "2":
            os.system("cls" if os.name == "nt" else "clear")
            #exibe a nova lista
            for n, nome in enumerate(nomes):
                print(f"Indice {n}: {nome}")
            break

        case _:
            print("Opção inválida")
            continue
        



