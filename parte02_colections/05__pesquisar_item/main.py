# PESQUISAR ITENS DA LISTA
cidades  = [
    "Rio de Janeiro", 
    "Brasilia" ,
    "São Paulo" ,
    "Goiânia" ,
    "Cuiabá" ,
    "Taguatinga" ,
    "Gama" ,
    "Belo Horizonte" , 
    "Fortaleza" , 
    "Recanto Das Emas" ,
    "Riacho Fundo" , 
    "Plano Piloto" , 
    "São Luis" , 
    "Ceilândia" , 
    "São Paulo" , 
    "Gama" , 
    "Recanto Das Emas"
]


# usuário informa nome a ser pesquisado
item = input("Informe a cidade a ser pesquisada: ").strip().title()

#verifica quantas vezes o termo foi encontrado e informa na tela
print(f"{item} foi encontrdo {cidades.count(item)} vezes na lista.")
