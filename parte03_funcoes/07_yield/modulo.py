# YIELD - Em Python, a palavra-chave yield é usada para transformar uma função comum em um gerador (generator), permitindo que ela retorne uma sequência de valores sob demanda em vez de calcular e guardar todos eles na memória de uma vez.

#bibliotecas
import os
import math

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def eq_2o_grau(a, b, c):
    delta = (b**2)-(4*a*c)
    if delta > 0:
        x1 = (-b+math.sqrt(delta))/(2*a)
        x2 = (-b+math.sqrt(delta))/(2*a)
        yield x1
        yield x2

    elif delta == 0:
        x = -b/(2*a)
        yield x 

    else:
        yield "não existem raízes reais."

        