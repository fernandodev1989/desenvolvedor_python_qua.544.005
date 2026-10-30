from modulo import limpar, peso_astro

#TODO: parte 03 atividade 01
'''
Crie um programa que calcule o peso de uma pessoa em um planeta do sistema solar escolhida por ela.
'''
# NOTE: Pesquisa pela aceleração da gravidade em cada planeta.
# NOTE: Inclua a lua na lista de planetas

def main():
    astros = {
        'mercurio': 3.73,
        'venus': 8.73,
        'terra': 9.8,
        'lua': 1.62,
        'marte': 3.73,
        'jupiter': 24.92,
        'saturno': 10.5,
        'urano': 8.73,
        'netuno': 11.77,

    }

    limpar()

    massa = float(input("Informe sua massa muscular em kg: ").replace(".",","))


    for chave, valor  in astros.items():
        print(f"{chave.upper()}:")
        print(f"Gravidade: {valor} m/s²")
        print(f"Peso: {peso_astro(massa,valor):.2f} N")
        print(f"{'-'*40}")

    


if __name__ == "__main__":
    main()

