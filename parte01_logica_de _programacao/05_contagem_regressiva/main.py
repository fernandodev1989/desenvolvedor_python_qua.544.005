# inporta as bibliotecas 
import os #ELE TRAS A FUNÇÃO SYSTEM 
import time #TRAS A FUNÇÃO SLEEP

# limpa o terminal
os.system("cls")

# declaração de variavel - entrada de dados
n = int(input("Informe um número inteiro: "))

#contador
while n >= 0:       #Laço de repertição WHILE
    os.system("cls")
    print(f"{n}...")
    time.sleep(1)
    n -= 1
print("BOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOM!!!!")