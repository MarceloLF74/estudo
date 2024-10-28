M = 'Matutino'
V = 'Vespertino'
N = 'Noturno'
turno = input('Qual turno você estuda? (Matutino, Vespertino, Noturno): ')
if turno == M:
    print('Bom dia!')
elif turno == V:
    print('Boa tarde!')
else:
    print('Boa noite')