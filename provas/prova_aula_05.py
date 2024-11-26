numero_de_alunos = int(input('Digite o número total de alunos da disciplina para calcular a média das notas: '))
notas = 3

nomes = []
medias = []


for i in range(numero_de_alunos):
    nome = input('Digite seu nome: ')
    nomes.append(nome)
    media = 0
    for j in range(notas):
        media += float(input(f'Digite sua nota {j+1} do aluno {nome}: '))
    media /= notas
    medias.append(media)
   
print('\nA média dos alunos foi:')
for i in range(numero_de_alunos):
    print(f'Aluno {nomes[i]}: {medias[i]}')
    if medias[i] >= 7:
        print('APROVADO')
    else:
        print('REPROVADO')

resultado = sum(medias) / (numero_de_alunos)
print(f'\nA media geral da turma foi {resultado}')