'''
5. Desenvolva um programa que solicite ao usuário os comprimentos dos três lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno. 
equilátero: todos os lados com o mesmo valor 
isósceles: dois lados com o mesmo valor
 escaleno: todos os lados com medidas distintas.
'''

print('Informe os comprimentos de cada lado do triângulo (em cm):')
lado1 = float(input('Lado 1: '))
lado2 = float(input('Lado 2: '))
lado3 = float(input('Lado 3: '))

if lado1 == lado2 == lado3: 
    print('Triângulo equilátero')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('Triângulo isósceles')
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print('Triângulo escaleno')

