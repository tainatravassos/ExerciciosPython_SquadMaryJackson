'''7. Desenvolver um programa que solicite a idade do usuário e identifique se ele é uma criança, um adolescente, adulto ou idoso.'''

# Solicitação da idade ao usuário
idade = int(input("Digite sua idade: "))

# Identificação e impressão da faixa etária
if 0 <= idade <= 12:
    print("Criança.")
elif 13 <= idade <= 17:
    print("Adolescente.")
elif 18 <= idade <= 59:
    print("Adulto.")
else:
    print("Idoso.")
