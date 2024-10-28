# import random

# #Lista com as opções
# opcoes = ['pedra', 'papel', 'tesoura']

# #Sorteia uma opção
# escolha = random.choice(opcoes)

# jogador = input('Escolha pedra, papel ou tesoura: ')

# for jogador in opcoes >= 'pedra':
#     print('Você venceu')

# for jogador in opcoes <= 'papel':
#     print('Você venceu')
    
# for jogador in opcoes == 'tesoura':
#     print('Você venceu')
    
# print('Quer jogar novamente?')


# import random

# # #Lista com as opções
# opcoes = ['pedra', 'papel', 'tesoura']

# # #Sorteia uma opção
# # escolha = random.choice(opcoes)
# escolha = 'pedra'

# # Escolha do jogador
# jogador = input('Escolha pedra, papel ou tesoura: ')

# # # Escolha se quer jogar novamente
# # sim = 's'
# # nao = 'n'

# # while jogador == 'pedra':
# #     if escolha == 'pedra':
# #         print('Empate')
# #         input('Quer jogar novamente? (s)sim (n)não: ')
# #         if sim:
# #             print(input('Escolha pedra, papel ou tesoura: '))
# #         elif nao:
# #                 print('Obrigado, até a próxima')

# import random

# # #Lista com as opções
# opcoes = ['pedra', 'papel', 'tesoura']

# # #Sorteia uma opção
# # escolha = random.choice(opcoes)
# # escolha = 'pedra'

# # Escolha do jogador
# jogador = input('Escolha pedra, papel ou tesoura: ')

# # Escolha se quer jogar novamente
# jogar_novamente = input('Quer jogar novamente? (s)sim (n)não: ')
# sim = 's'
# nao = 'n'

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