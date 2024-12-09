class Carro:
    def __init__(self, marca: str, modelo: str, ano: int):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def exibir_dados(self):
        print(f'Seguem dados dos veículos: {self.marca}, {self.modelo}, {self.ano}')

carro_1 = Carro('Chevrolet', 'Camaro', 2012)
carro_2 = Carro('BMW', '750', 2015)

carro_1.exibir_dados()
carro_2.exibir_dados()