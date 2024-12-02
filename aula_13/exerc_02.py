temperaturas = (0, 32, 100)

celcius = list(map( lambda x: x 5 / 9 * (x - 32), temperaturas))
print(celcius)