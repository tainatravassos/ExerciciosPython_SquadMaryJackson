'''
  4. Implemente um programa que classifique um aluno com base em sua pontuação em um exame. O programa deverá solicitar uma nota de 0 a 10. Se a pontuação for maior ou igual a 7, o aluno é aprovado; caso contrário, é reprovado.
'''


grade = float(input('Digite sua nota:'))

if grade >=0 and grade <=10:
  if grade >= 7:
    print(f'Parabéns você foi aprovado! Sua note foi {int(grade)}')
  else:
    print(f'Infelizmente você foi reprovado! Sua nota foi {int(grade)}')
else:
  print('Valor inválido!\nPor favor, digite um valor entre 0 e 10.')