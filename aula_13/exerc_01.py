precos = [10, 50, 100, 45.99]

desconto = list(map(lambda x: round(x * .90, 2), precos))
print(desconto)