pessoa = {
    'nome': 'Ana',
    'idade': 25,
    'cidade': 'São Paulo',
}

for itens, significado in pessoa.items():
    print(f'{itens}: {significado}')

contato = {
    'telefone': '123456789',
    'email':'contato@exemplo.com',
}

contato['telefone'] = ['987654321']

print(contato)

aluno = {
    'nome': 'João',
    'nota': 7.5
}

aluno['curso'] = 'Matemática'

print(aluno)

produto = {
    'nome': 'Laptop',
    'preço': 3500,
    'quantidade': 10,
}

del produto ['quantidade']

print(produto)