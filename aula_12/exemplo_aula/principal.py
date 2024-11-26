from operacoes import aumentar_preco

macarrao = 5
frango = 20.1

# aumentar 10% em todos os preços
novo_preco_macarrao = aumentar_preco(macarrao, 10)
novo_preco_frango = aumentar_preco(frango, 10)

print(f'Novo preço macarrão: R$ {novo_preco_macarrao}')
print(f'Novo preço frango: R$ {novo_preco_frango}')

