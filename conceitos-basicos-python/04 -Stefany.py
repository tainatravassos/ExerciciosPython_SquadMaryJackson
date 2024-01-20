'''4. Receba do usuário a quantidade de litros de combustível consumidos e a distância percorrida. Calcule e imprima o consumo médio em km/l.'''

#Pergunta ao usuário
litros_consumidos = float(input("Digite a quantidade de combustivel consumido: "))
distancia_percorrida = float(input("Digite a distancia percorrida em km: "))

#Cálculo do consumo médio
consumo_medio = distancia_percorrida/ litros_consumidos

#Impressão do resultado
print(f"O consumo médio é de {consumo_medio:.2f} km/l.")


