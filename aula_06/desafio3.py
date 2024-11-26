print('Bem vindo ao jogo FizzBuzz! Você deve contar de 1 a 35. Nos números múltiplo de 3, você deve dizer Fizz.')
print('Nos números múltiplo de 5, você deve dizer Buzz. Se o número for múltiplo de ambos, deve dizer FizzBuzz.')

for i in range(1, 36):
    if i % 3 == 0 and i % 5 == 0:
        resultado = input(f'{i}: ')
        if resultado != 'FizzBuzz':
            print('Você errou!')
            break
    elif i % 3 == 0:
        resultado = input(f'{i}: ')
        if resultado != 'Fizz':
            print('Você errou!')
            break
    elif i % 5 == 0:
        resultado = input(f'{i}: ')
        if resultado != 'Buzz':
            print('Você errou!')
            break
    else:
        resultado = input(f'{i}: ')
        if resultado != str(i):
            print('Você errou!')
            break
else:
    print('Você ganhou o jogo FizzBuzz! Parabéns!')