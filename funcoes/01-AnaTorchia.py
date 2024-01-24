#1. Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def soma3(x,y,z):
 return x+y+z

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
num3 = int(input('Digite o terceiro numero: '))

calculo = soma3(num1, num2, num3)
print (f'O resultado da soma é:{calculo}')