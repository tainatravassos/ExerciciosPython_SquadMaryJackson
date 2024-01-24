'''
10. Faça um Programa que utilize 4 variáveis como preferir e no final print uma mensagem amigável utilizando as variáveis criadas. 
Exemplos de variáveis: nome, idade, lugar, profissão ....
Exemplo de retorno: Olá Maria, prazer te conhecer. Sou de São Paulo também e estou migrando de área. 
'''

nome = input('Informe seu nome: ')
curso = input('Informe seu curso: ')
nota1 = float(input('Informe a nota 1: '))
nota2 = float(input('Informe a nota 2: '))

media = (nota1 + nota2) / 2 #Cálculo da média das notas

if media >= 6:
    print('\nOlá, {}!'.format(nome))
    print('Parabéns, você foi aprovada no curso {}!'.format(curso))
    print(f'Sua média final foi {media:.1f}')

else: 
    print('\nOlá, {}!'.format(nome))
    print('Você foi reprovada no curso {} :( '.format(curso))
    print(f'Sua média final foi {media:.1f}')

