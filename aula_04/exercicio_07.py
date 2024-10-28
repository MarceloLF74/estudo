

palavra = input(f'Digite uma palavra: ')
contagem = 0

for letra in palavra:
    if letra == 'a':
        contagem += 1

print(f'A palavra {palavra} tem {contagem} letra(s) {letra}')