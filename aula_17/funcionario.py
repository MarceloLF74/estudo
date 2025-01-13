class Funcionario:
    def __init__(self, nome: str, salario: float, departamento: str):
        self.nome = nome
        self.salario = salario
        self.departamento = departamento


    def mostrar_informacoes(self):
        print(f'Nome: {self.nome}')
        print(f'Salário: {self.salario}')
        print(f'Departamento: {self.departamento}')


class Gerente(Funcionario):
    def __init__(self, nome: str, salario: float, departamento: str, bonus: float):
        super().__init__(nome, salario, departamento)
        self.bonus = bonus

    def mostrar_informacoes(self):
        print(f'Nome: {self.nome}')
        print(f'Salário: {self.salario}')
        print(f'Departamento: {self.departamento}') 
        print(f'Bonus: {self.bonus}%')

class Analista(Funcionario):
    def __init__(self, nome: str, salario: float, departamento: str, area_analise: str):
        super().__init__(nome, salario, departamento)
        self.area_analise = area_analise    

    def mostrar_informacoes(self):
        print(f'Nome: {self.nome}')
        print(f'Salário: {self.salario}')
        print(f'Departamento: {self.departamento}') 
        print(f'Área de Análise: {self.area_analise}')

class Assistente(Funcionario):
    def __init__(self, nome: str, salario: float, departamento: str, horario_trabalho: float):
        super().__init__(nome, salario, departamento)
        self.horario_trabalho = horario_trabalho
    
    def mostrar_informacoes(self):
        print(f'Nome: {self.nome}')
        print(f'Salário: {self.salario}')
        print(f'Departamento: {self.departamento}') 
        print(f'Horário de trabalho: {self.horario_trabalho}h')





gerente_1 = Gerente('Fábio', 10000, 'RH', 15)
gerente_1.mostrar_informacoes()
print('-'*100)
funcionario_1 = Funcionario('Joana', 4500, 'Dev Jr')
funcionario_1.mostrar_informacoes()
print('-'*100)
analista_1 = Analista('João', 5500, 'Analista', 'Analista financeiro')
analista_1.mostrar_informacoes()
print('-'*100)
assistente_1 = Assistente('Pedro', 3500, 'Diretoria', 8)
assistente_1.mostrar_informacoes()
