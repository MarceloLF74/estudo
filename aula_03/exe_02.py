frase = "Bem vindo(a) ao mundo Python!"
contagem = 0

for letra in frase:
    if letra == "y":
        contagem += 1

print(f"A letra {letra} aparece {contagem} vezes na frase.")