import os


# TODO: parte 03 atividade 02
'''
Crie um programa em que o usuário informa um número inteiro eo programa retorne a sequência Fivonacci.
'''

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def fibonacci(n):
    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

def main():
    n = int(input("Informe o número de sequências Fibonacci: "))
    print(fibonacci(n))



if __name__ == "__main__":
    main()

