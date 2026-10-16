# ATIVIDADE 01
'''
CRIE UM PROGRAMA QUE RECEBA O NOME, A MASSA EM KG E A ALTURA EM METROS DO USÚARIO, CALCULE SEU IMC E FINALIZE INFORMANDO O DIAGNOSTICO DO USÚARIO COM BASE DO VALOR DO IMC( SE ESTÁ MAGRO, GORDO OU PESO IDEAL)
'''
nome = input(" Digite seu nome ").strip().title()
altura = float(input(" Digite sua altura ").replace(",","."))
peso = float(input(" Digite seu peso ").replace(",","."))

imc = peso / (altura * altura)

if imc <= 18.5:
    print("Magro!")

elif imc <= 24.9:
    print("Peso norma!")

elif imc <= 29.9:
    print("Sobrepeso!")

elif imc <= 34.9:
    print("Obesidade grau 1!")

elif imc <= 39.9:
    print("Obesidade grau 2!")

else:
    print("Grave")

    
