#dicionario
usuario = {
    'nome': "fernando Menezes",
    'idade': 37,
    'email': "fernando@menezes.com",
    'telefone': "(62) 98658-8965",
    'endereço': "Campo da esperança"
}

# exibi a lista original
for chave, valor in usuario.items():
    print(f"{chave}: {valor}")

# informar a  chave a ser deletada
chave_escolhida = input("Infoeme a chave a excluir: ").strip().lower()

# deleta a chave
del usuario[chave_escolhida]

# re-exibe ao novo dicionario
for chave, valor in usuario.items():
    print(f"{chave}: {valor}")
    