palavra = input('Digite uma palavra: ')

for letra in palavra:
    if letra not in 'aeiou':
        print(letra)
        break