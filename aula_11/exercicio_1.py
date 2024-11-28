def adicionar_tarefa(descricao_informada: str):
    tarefa_nova = {
        'descricao': descricao_informada,
        'status': 'pendente'
    }
    tarefas.append(tarefa_nova)

def adicionar_tarefa(descricao_informada: str):
    tarefa_nova = {
        'descricao': descricao_informada,
        'status': 'pendente'
    }
    tarefas.append(tarefa_nova)

def listar_tarefas(tarefas: list):
    if tarefas == []:
        print('Nenhuma tarefa disponível')
    else:
        for indice, tarefa in enumerate(tarefas, start=1):
            print(f'[{indice}] {tarefa['descricao']} - {tarefa['status']}')

def marcar_concluida(indice_escolhido: int, tarefas: list):
    if indice_escolhido <= 0 or indice_escolhido > len(tarefas):
            print('Índice inválido!')
    for indice, tarefa in enumerate(tarefas, start=1):
        if indice_escolhido == indice:
            tarefas[0]['status'] = 'Concluído'
        return tarefas

def remover_tarefa(indice_escolhido: int, tarefas: list):
    for indice, tarefa in enumerate(tarefas, start=1):
        if indice_escolhido == indice:
            del tarefas[indice-1]
    return tarefas
    
tarefas = [
    {'descricao': 'Estudar Python', 'status': 'Pendente'}, 
    {'descricao': 'Fazer supermercado', 'status': 'Concluído'}
]


# Passo 2: Adicionar uma tarefa

descricao_tarefa = input('Digite uma tarefa para adicioná-la à lista: ')
adicionar_tarefa(descricao_tarefa)
print(tarefas) 


# Passo 3: Listar tarefas

# listar_tarefas(tarefas)


# Passo 4 : Marcar uma tarefa como concluída

for indice, tarefa in enumerate(tarefas, start=1):
    print(f'[{indice}] {tarefa['descricao']} - {tarefa['status']}')
indice_escolhido = int(input('Qual tarefa você concluiu? '))
resultado = marcar_concluida(indice_escolhido, tarefas)
print(resultado)


# Passo 5: Remover tarefa

for indice, tarefa in enumerate(tarefas, start=1):
    print(f'[{indice}] {tarefa['descricao']} - {tarefa['status']}')
indice_escolhido = int(input('Qual tarefa você deseja remover? '))
resultado = remover_tarefa(indice_escolhido, tarefas)
print(resultado)








