# lista de dicionarios
usuarios = [
    {
        'nome': "Fernando Silva",
        'idade': 37,
        'email': "fernando@silva.com"
    },
    {
        'nome': "Maria Joana",
        'idade': 36,
        'email': "mari@joana.com"
    },
    {
        'nome': "Jose Soares",
        'idade': 63,
        'email': "jose@barbosa.com" 
    }
]

for usuario in usuarios:
    for chave, valor in usuario.items():
        print(f"{chave.capitalize()}: {valor}")
    print(f"{'-'*40}")
