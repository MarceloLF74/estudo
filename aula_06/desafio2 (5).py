while True:
    
    import random

    opcoes = ['pedra', 'papel', 'tesoura']
    escolha = random.choice(opcoes)
    jogador = input('Escolha pedra, papel ou tesoura: ')
    sim = 's'
    nao = 'n'

    
    if jogador == escolha:
        print('Empate')
    elif jogador == 'pedra' and escolha == 'tesoura':
        print('Você venceu')
    elif jogador == 'papel' and escolha == 'pedra':
        print('Você venceu')
    elif jogador == 'tesoura' and escolha == 'papel':
        print('Você venceu')
    else:
        print('Você perdeu')

    jogar_novamente = input('Quer jogar novamente? (s)sim (n)não: ')
    
    if jogar_novamente != sim:
            print('Obrigado, até a próxima')
            break