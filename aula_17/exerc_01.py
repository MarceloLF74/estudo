class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def apresentar(self, pessoa):
        print(f'Olá, meu nome é {pessoa.nome} e tenho {pessoa.idade} anos')

class Estudante:
    

pessoa_01 = Pessoa('Marcelo', 50)
pessoa_02 = Pessoa('Fernando', 2)
pessoa_01.apresentar(pessoa_01)
pessoa_02.apresentar(pessoa_02)

