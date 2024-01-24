'''
10. Faça um programa que lê três números inteiros e os mostra em ordem crescente.
'''

num1 = float(input('Valor 1: '))
num2 = float(input('Valor 2: '))
num3 = float(input('Valor 3: '))

# Maior
if num1 > num2 and num1 > num3:
    maior = num1
elif num2 > num1 and num2 > num3:
    maior = num2
else:
    maior = num3

# Menor
if num1 < num2 and num1 < num3:
    menor = num1
elif num2 < num1 and num2 < num3:
    menor = num2
else:
    menor = num3

# Médio
if num1 > num2 and num1 < num3:
    medio = num1
elif num1 < num2 and num1 > num3:
    medio = num1
elif num2 < num1 and num2 > num3:
    medio = num2
elif num2 > num1 and num2 < num3:
    medio = num2
else:
    medio = num3

# Saídas
print('\nNúmeros em ordem crescente: ')
print(menor)
print(medio)
print(maior)