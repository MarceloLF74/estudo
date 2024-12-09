class Pessoa:
    def __init__(self, nome: str, idade: int, idioma: str):
        self.nome = nome
        self.idade = idade
        self.idioma = idioma
    
    def apresentar(self):
        print(f'Oi, meu nome é {self.nome}, tenho {self.idade} anos e estou aprendendo {self.idioma}')

pessoa_01 = Pessoa('Ana', 25, 'Inglês')
pessoa_02 = Pessoa('Carlos', 30, 'Espanhol')

pessoa_01.apresentar()
pessoa_02.apresentar()