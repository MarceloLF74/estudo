# Faça um programa que peça ao usuário o tempo do carro dele.

#se tiver até 3 anos ele será novo.
#se o carro tiver entre 4 e 5 anos, ele será seminovo
#mais de 5, será velho

idade = int(imput('Digite a idade do carro'))

if idade <= 3:
    print('Carro novo!')
elif idade <= 4 and idade <= 5:
    print('Seminovo')
else:
    print('Carro velho!')