# Map é uma função que é criada em cima de uma lista.
import os

limpar = lambda: os.system("cls" if os.name == "nt" else "clear")
pg = lambda x: x*2 

def main():
    # Lista original
    numeros = [1,2,3,4,5,6,7,8,9]

    limpar()
    print(numeros)

    numeros_pg = list(map(pg, numeros))

    # evibe a nova lista coma pg aplicado
    print(f"Nova lista com pg: {numeros_pg}")


if __name__ == "__main__":
    main()
    
