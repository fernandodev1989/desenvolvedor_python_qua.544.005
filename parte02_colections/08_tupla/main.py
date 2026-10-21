# Tupla -  usa a lista com parenteses e não com colchetes como as outras.
# A lista não pode modificada de nenhuma forma. 
dias_da_semana = (
    "Domingo",
    "Segunda-Feira",
    "Terça-Feira",
    "Quarta-Feira",
    "Quinta-Feira",
    "Sexta-Feira",
    "Sábado"
)

# exibe a tupla
for dia in dias_da_semana:
    print(dia)

# NOTE: se tentar alterar a tupla, o programa retorna erro. Exemplo
try:
    dias_da_semana.sort()
    for dia in dias_da_semana:
        print(dia)
except Exception as e:
    print(f"Não foi possivel ordenar. {e}, ")
finally:
    print("programa encerrado.")
