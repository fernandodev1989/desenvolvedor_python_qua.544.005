#TODO: parte 03 atividade 01
'''
Crie um programa que calcule o peso de uma pessoa em um planeta do sistema solar escolhida por ela.
'''
# NOTE: Pesquisa pela aceleração da gravidade em cada planeta.
# NOTE: Inclua a lua na lista de planetas

import os
import math


def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def calcular_peso(massa, gravidade):
    return massa * gravidade

