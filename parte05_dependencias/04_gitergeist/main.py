import time
from datetime import date
import pyautogui as auto

# Define a variável 'hoje' (caso ainda não tenha definido no seu código)
hoje = date.today().strftime("%d/%m/%Y")

# Abre o CMD
auto.hotkey("win", "r")
time.sleep(0.5)
auto.write("cmd")
auto.press("enter")
time.sleep(1.5) # Espera o terminal abrir

# Entra na pasta (com aspas por causa dos espaços no nome)
auto.write('cd "C:\\Users\\ALUNO\\Fernando da Silva Menezes Barbosa\\Workspaces\\Python\\desenvolvedor_python_qua.544.005"')
auto.press("enter")
time.sleep(0.5)

# Comandos do Git
auto.write("git add .")
auto.press("enter")
time.sleep(1)

auto.write(f'git commit -m "Aula do dia {hoje}"')
auto.press("enter")
time.sleep(2)

auto.write("git push")
auto.press("enter")
time.sleep(5) # Tempo extra para a internet enviar os arquivos

# Fecha o terminal
auto.write("exit")
auto.press("enter")
