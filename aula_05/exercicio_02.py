while True:
    nota_valida = float(input('Por favor, digite uma nota entre 0(zero) e 10(dez)10: '))
    if nota_valida >= 0 and nota_valida <= 10:
        print(f'Você digitou uma nota válida: {nota_valida}')
        break
    else:
        print(f'Você digitou uma nota inválida. ')