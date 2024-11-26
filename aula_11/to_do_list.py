def adicionar_tarefa(descricao_informada: str):
    tarefa_nova = {
        'descricao': descricao_informada,
        'status': 'pendente'
    }
    tarefas.append(tarefa_nova)

def listar_tarefas(lista_de_tarefas: list):
    if tarefas == []:
        print('Nenhuma tarefa disponível')
    else:
      for indice, tarefa in enumerate(lista_de_tarefas, start=1):
        print(f'[{indice}] - {tarefa['descricao']} - {valor['status']}')

def marcar_concluida():
   for indice in tarefas:
      

indice_escolhido = input('Qual tarefa você deseja concluir? ')

tarefas = [
    {'descricao': 'estudar python', 'status': 'pendente'},
    {'descricao': 'fazer supermercado', 'status': 'concluído'},
    ]

descricao_tarefa = input('Digite a descrição da nova tarefa: ')
adicionar_tarefa(descricao_tarefa)

# print(tarefas)

# else:
#     for indice, valor in enumerate(tarefas, start=1):
#         print(f'[{indice}] - {valor['descricao']} - {valor['status']}')

