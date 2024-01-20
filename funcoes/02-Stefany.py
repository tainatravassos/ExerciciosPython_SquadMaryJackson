'''2. Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.'''

# Definição da função que retorna o reverso de um número inteiro
def reverso_numero(numero):
    return int(str(numero)[::-1])

# Exemplo de uso da função
numero = 127
resultado = reverso_numero(numero)
print(f"O reverso de {numero} é: {resultado}")
