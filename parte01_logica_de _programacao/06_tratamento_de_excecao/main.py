# Tratamento de exceção

try: 
   # pass # Diz ao sistema para ignorar 
   nome = input("Informe seu nome: ").strip().title()
   idade = int(input("Informe sua idade: "))

   print(f"Nome do usuario: {nome}")
   print(f"Idade do usúario: {idade} anos,")
except Exception as e: 
    print(f"Não foi possível executar a ação! {e} ")
finally:
    print("Programa finalizado com sucesso")


# Forma de localizar erro

# Colocar o try no inicio e "except Exception as e" no final -  o que tiver dentrro dele será lido e indentificado o erro.

'''try:
       # TODO: Parte a se concluida no codigo
except Exception as e: 
    print("sistema de erro"")

   # FIXME: a linha abaixo está errada 
'''