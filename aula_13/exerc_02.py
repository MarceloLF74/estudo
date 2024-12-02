temperaturas = [0, 32, 100]

celcius = list(map(lambda x: round((5 / 9 * (x - 32)),2), temperaturas))
print(celcius)