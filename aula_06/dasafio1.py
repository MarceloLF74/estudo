numero = int(input('Digite um número aleatório entre 1 e 20: '))

import random
numero_secreto = random.randint(1, 20)
# numero_secreto = 4 


while numero != numero_secreto:
    
    if numero < numero_secreto:
        print('O número foi muito baixo')
        numero = int(input('Digite um número aleatório entre 1 e 20: '))
    
    elif numero > numero_secreto:
        print('O número foi muito alto')
        numero = int(input('Digite um número aleatório entre 1 e 20: '))

print('O número está correto')