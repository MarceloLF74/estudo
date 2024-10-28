# 1 = Verao
# 2 = Verao
# 3 = Outono
# 4 = Outono
# 5 = Outono
# 6 = Inverno
# 7 = Inverno
# 8 = Inverno
# 9 = Primavera
# 10 = Primavera
# 11 = Primavera
# 12 = Verao
# int(input(f'Digite o mês do ano: '))
# if == 3,4,5:
#     print()


 
estacao_do_ano = int(input(f'Digite o mês do ano: '))
if estacao_do_ano == 1 or estacao_do_ano == 2 or estacao_do_ano == 12:
    print('Verão')
elif estacao_do_ano >= 3 and estacao_do_ano <= 5:
    print('Outono')
elif estacao_do_ano >= 6 and estacao_do_ano <= 8:
    print('Inverno')
else:
    print('Primavera')
