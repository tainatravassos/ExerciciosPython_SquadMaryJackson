'''
6. Vamos construir um jogo de forca. O programa escolherá aleatoriamente uma palavra secreta de uma lista predefinida. 
A palavra secreta será representada por espaços em branco, um para cada letra da palavra. 
O jogador terá um número limitado de 6 tentativas. Em cada tentativa, o jogador pode fornecer uma letra. 
Se a letra estiver presente na palavra secreta, ela será revelada nas posições correspondentes. 
Se a letra não estiver na palavra, uma mensagem de erro deverá ser informada. 
Após um número máximo de erros, o jogador perde. 
O jogo continua até que o jogador adivinhe a palavra ou exceda o número máximo de tentativas. 
Dica: Você precisará importar uma biblioteca para resolver esse exercício
'''

import random

def escolher_palavra():
    palavras = ["python", "casa", "jogo", "forca", "escola"]
    return random.choice(palavras)

def exibir_palavra(palavra, letras_corretas):
    exibicao = ""

    # Percorre a palavra e verifica se a letra existe na palavra secreta
    # Se sim, a letra é exibida. Se não, exibe um traço
    for letra in palavra: 
        if letra in letras_corretas:
            exibicao += letra + " "
        else:
            exibicao += "_ "
    return exibicao.strip() # Strip -> remove os espaços em branco no fim e início 

def jogar_forca():
    palavra_secreta = escolher_palavra()
    letras_corretas = []
    letras_erradas = []
    erros = 0
    tentativas_maximas = 6
    tentativas = 0

    print("**********\nBem-vindo ao Jogo da Forca!\n**********")
    print('Palavra selecionada: ')
    print(exibir_palavra(palavra_secreta, letras_corretas))

    while tentativas <= tentativas_maximas:        
        letra = input("\nDigite uma letra: ").lower() # lower = conversão maiúscula e minúscula

        # interrompe a execução do loop atual e passar para o próximo caso seja uma letra já usada antes
        if letra in letras_corretas or letra in letras_erradas: 
            print("Você já tentou essa letra. Tente outra.")
            continue 

        tentativas += 1
        tentativas_restantes = tentativas_maximas - tentativas

        if letra in palavra_secreta:
            letras_corretas.append(letra) # Insere a letra na lista letras_corretas
            erros_restantes = 3 - erros 
        else:
            print("Letra incorreta. ")
            letras_erradas.append(letra) # Insere a letra na lista letra_erradas
            erros += 1
            erros_restantes = 3 - erros 
            if len(letras_erradas) > 3 and tentativas_restantes >= 0:
                print('Letras erradas: ', letras_erradas)
                print("\nVocê perdeu. Número máximo de erros atingido. \nA palavra era:", palavra_secreta)
                break

        print('\nPalavra: ',exibir_palavra(palavra_secreta, letras_corretas))
        print('Letras erradas: ', letras_erradas)

        if tentativas_restantes > 0: 
            print('Tentativas restantes: ', tentativas_restantes)
        elif set(letras_corretas) != set(palavra_secreta):
            if len(letras_erradas) == 3  or tentativas_restantes == 0: 
                print('Ultíma tentativa!')
        
        if erros_restantes <= 3:
            print('Erros restantes: ', erros_restantes)

        if set(letras_corretas) == set(palavra_secreta): # Conjunto de letras_corretas == conjunto de palavra_secreta
            print("\nParabéns! Você acertou a palavra:", palavra_secreta)
            break

    if tentativas_restantes < 0 and set(letras_corretas) != set(palavra_secreta):
        print("\nVocê perdeu. Número máximo de tentativas atingido. \nA palavra era:", palavra_secreta)

jogar_forca()
