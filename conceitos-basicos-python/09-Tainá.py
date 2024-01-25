'''09. Solicite ao usuário o número de horas de exercício físico por semana. Calcule o total de calorias queimadas em um mês, 
considerando uma média de 5 calorias por minuto de exercício.'''

horas_s=int(input('Quantas horas por semana você faz exercício físico? '))
h_minutos=horas_s*60 #convertendo h em min
calorias=h_minutos*5 
um_mes= calorias*4 #1mês tem em média 4semanas

print(f'Parabéns! Você perde cerca de {um_mes} calorias por mês.')
