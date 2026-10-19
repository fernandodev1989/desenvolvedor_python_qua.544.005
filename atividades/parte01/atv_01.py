# ATIVIDADE 01
'''
CRIE UM PROGRAMA QUE RECEBA O NOME, A MASSA EM KG E A ALTURA EM METROS DO USÚARIO, CALCULE SEU IMC E FINALIZE INFORMANDO O DIAGNOSTICO DO USÚARIO COM BASE DO VALOR DO IMC( SE ESTÁ MAGRO, GORDO OU PESO IDEAL)
'''
nome = input(" Digite seu nome ").strip().title()
altura = float(input(" Digite sua altura ").replace(",","."))
massa = float(input(" Digite seu peso ").replace(",","."))

imc = massa / (altura * altura)

if imc <= 18.5:
    print(f"Magro! IMC {imc:.2f}")

elif imc <= 24.9:
    print(f"Peso norma! IMC {imc:.2f}")

elif imc <= 29.9:
    print(f"Sobrepeso! IMC {imc:.2f}")

elif imc <= 34.9:
    print(f"Obesidade grau 1! IMC {imc:.2f}")

elif imc <= 39.9:
    print(f"Obesidade grau 2! IMC {imc:.2f}")

else:
    print(f"Grave! IMC {imc:.2f}")

    
