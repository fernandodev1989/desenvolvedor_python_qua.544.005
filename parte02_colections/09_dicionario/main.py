# dicionário - usa chaves
usuario = {
    'nome': "Fernando da Silva",
    'idade': 37,
    'altura': 1.83,
    'email': "fernando@email.com",
    'cpf': "123.456.789-12",
    'telefone': "(61) 98765-4321"

}
# exibe valor espécifico - vantagem dessa forma e póssivel alterar os dados /desvantagem não aceita erros - tem que usar TRY EXCEPTION
print(f"Nome: {usuario['nome']}")
# outra forma de exibir - vantagem aceita entrada errada sem travar / desvantagem não aceita mudar os dados - NÃO PRECISA USAR O TRY EXCEPTION
print(f"E-mail: {usuario.get('email')}")

# Outra forma em loop - percorrendo o dicionario - mosta tudo.
for chave, valor in usuario.items():
    print(f"{chave.capitalize()}: {valor}.")

    