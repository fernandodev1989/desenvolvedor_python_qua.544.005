# LISTA DE TAREFAS 

# Biblioteca
import os


tarefas = []# Lista vazia


# Limpar o terminal
os.system("cls" if os.name == "nt" else "clear")


# loop
while True:
    # Menu 
    print("1 - Inserir nova tarefa na lista")
    print("2 - Finalizar e exibir lista")
    opcao = input("Opção desejada: ").strip() # informa a opção desejada


    # verifica a opção informada
    match opcao:
        case "1":
            nova_tarefa = input("Informe a nova tarefa: ") # usuário informa novo item
            tarefas.append(nova_tarefa) #inseri item na lista
            continue # retorna para o inicio do loop
        case "2":
            os.system("cls" if os.name == "nt" else "clear") # Limpa 


            # exibe a lista
            for n, tarefa in enumerate(tarefas, start=1):
                print(f"{n}° tarefa: {tarefa}")
            break #encerra o loop
