numero_programa = 7
tentativas = 3
jogador = 0

while jogador < tentativas:

    jogo = int(input('Adivinhe o número que o computador escolheu. Você tem até 3 tentativas pra adivinhar: '))
    
    jogador += 1
    
    if jogo == numero_programa:
        print('Parabéns! Você acertou!')
        break
    
    else:
        print('Você errou!')