print('Insira dois números inteiros, representando o início e o fim do intervalo. O computador verificará a existêncica de numeros pares e fará a soma deles.')

numero_inicio = int(input('Insira o primeiro numero: '))
numero_fim = int(input('Insira o segundo numero: '))

soma = 0
pares = False

for numero in range(numero_inicio, numero_fim + 1):
    if numero % 2 == 0:
        soma += numero
        pares = True

if pares:
    print(f'A soma dos número de {numero_inicio} a {numero_fim} é igual a', soma)

else:
    print('Não tem números pares nesse intervalo')




# soma = 0
# numero = 1
# while numero <= 10:
#     soma += numero
#     numero += 1
# print('A soma dos número de 1 a 10 é igual a', soma)




# while numero_inicio <= numero_fim:
#     for a in range({numero_inicio}, {numero_fim}):
#         for b in range({numero_inicio}, {numero_fim}):
#             if ({numero_inicio} + {numero_fim}) % 2 == 0:
#                 soma_pares += a
#             print(soma_pares)
    

