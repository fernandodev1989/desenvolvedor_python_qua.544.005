# Inserir nova chave
usuario = {
    'nome': "Julia Ramos",
    'idade': 9,
    'email': "julia@email.com"
}


# usuario informa o nome da chave
nova_chave = input("Informe o nome da nova chave: ").strip().lower()
# usuario informa o valor da nova chave
usuario[nova_chave] = input("Informe o valor da nova chave: ").strip()


# exibe o dicionario
for chave, valor in usuario.items():
    print(f"{chave.capitalize()}: {valor}.")



