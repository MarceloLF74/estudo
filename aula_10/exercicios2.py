#exercicio1
calcular_desconto = lambda x, y: x * ((100-y)/100)
print(calcular_desconto(100, 15))

#exercicio2
converter_real_para_dolar = lambda x, y: x * y
print(converter_real_para_dolar(100, 5.2))

#exercicio3
def temperatura_conforto (x):
    if x >= 18 and x <= 25:
        print('A temperatura está ok.')
    else:
        print('A temperatura está fora da faixa de conforto')

temperatura_conforto(19.5)

#exercicio4
