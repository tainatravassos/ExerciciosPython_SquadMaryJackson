'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.Calcule e mostre o total do seu salário no referido mês
'''


salaryByHour = float(input("Por favor,informe o seu salário por hora: "))
workHours = int(input("Por favor,informe a quantidade de horas trabalhadas no mês: "))

def salaryPerMonth() :
    salary = salaryByHour * workHours
    print(f'O seu salário mensal será de: R$ {salary:.2f}')


salaryPerMonth()