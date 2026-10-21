# dicionario
import os

usuario = {
    'nome': "fernando Menezes",
    'idade': 30,
    'email': "fernando@menezes.com",
    'telefone': "(62) 98658-8965"
}


# limpa terminal
os.system("cls" if os.name == "nt" else "clear")

# loop
while True:
    # exibe o dicionario
    for chave, valor in usuario.items():
        print(f"{chave}: {valor}")

    # informe o nome da chave a ser alterada
    #.lower converte as letras para minusculas - .strip retira os espaços
    chave_escolhida = input("Informer o nome da chave que deseja alterar ou enter para encerrar: ").strip().lower() 
    #verifica se a chave e válida
    if chave_escolhida:
        #informa outro valor
        usuario[chave_escolhida] = input("Informe o novo valor: ").strip()
        continue
    else:
        break





