# tarefas = ['arrumar a cama', 'pagar boleto', 'lavar louça', 'comprar carne', 'estudar programação']

# print(tarefas)

# usuario1 = input('Adicione uma nova tarefa a lista: ')
# tarefas.append(usuario1)

# print(tarefas)

# usuario2 = int(input('Informe o índice de uma tarefa que deseja remover da lista: '))

# tarefas2 = tarefas.pop(usuario2)

# print(tarefas2)

tarefas = ['arrumar a cama', 'pagar boleto', 'lavar louça', 'comprar carne', 'estudar programação']

print(tarefas)

usuario = input('Adicione uma nova tarefa a lista: ')
tarefas.append(usuario)

print(tarefas)

usuario2 = int(input('Informe o índice de uma tarefa que deseja remover da lista: '))

tarefas = tarefas.pop(usuario2)

print(tarefas)