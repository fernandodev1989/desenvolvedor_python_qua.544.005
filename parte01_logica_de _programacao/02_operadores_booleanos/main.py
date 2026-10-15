''' Operadores Booleanos
and = e - quando 2 ou mais condicionais seja true(verdadeira)
or = ou e quando tem 2 condicionais e apenas 1 precisa ser true (verdadeira)
not = não - quando a condição for false
'''

# declarações de variaveis
nome = input("Informe seu nome").strip().title()
idade = int(input("Informe sua idade"))
altura = float(input("Informe sua altura em metros").replace(",","."))

# Verifica se o pagante possui os requisitos
if idade >= 12 and altura >= 1.35:
    print(f"{nome} está autorizado a entrar.")
else:
    print(f"{nome} não está autorizado entrar.")

# Como fazer o sistema aceitar a "," virgula utilize altura = float(input("Informe sua altura").replace(",","."))

