'''# Solicite ao usuário o peso em kg e a altura em metros. Calcule e
imprima o Índice de Massa Corporal (IMC) usando a fórmula:
IMC = peso / (altura x altura)'''
altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em quilogramas: "))
imc = peso / (altura * altura )
print("Seu IMC é: {:.2f}".format(imc))

