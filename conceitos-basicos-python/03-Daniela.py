'''
3. Faça um Programa que peça a quantidade de quilômetros, transforme em metros, centímetros e milímetros.
'''

km = float(input('Qtd. de quilômetros: '))
print('\nConversão em: ')

# Funções de conversão
def metros():
    m = km*1000
    print(f'Metros = {m:.2f}')

def centimetros():
    cm = km*100000
    print(f'Centímetros = {cm:.2f}')

def milimetros():
    mm = km*1000000
    print(f'Milímetros = {mm:.2f}')

# Chamada das funções
metros()
centimetros()
milimetros()