class Cliente:
    def __init__(self, nome: str, email: str, data_cadastro: str):
        self.nome = nome
        self.email = email
        self.data_cadastro = data_cadastro

    def mostrar_info():
        print(f'Nome: {self.nome}')
        print(f'email: {self.email}')
        print(f'Data de Cadastro: {self.data_cadastro}')

class ClientePremium(Cliente):
    def __init__(self, nome: str, email: str, data_cadastro: float, limite_credito: float):
        super().__init__(nome, email, data_cadastro)
        self.limitecredito = limite_credito

    def mostrar_info():
        print(f'Nome: {self.nome}')
        print(f'email: {self.email}')
        print(f'Data de cadastro: {self.data_cadastro}')
        print(f'Limete de crédito: {self.limite_credito}')


cliente_1 = Cliente('Maria', 'maria@gmail.com', 01.01.2025)
cliente_1.mostrar_info()
print('-')*100
cliente_2 = ClientePremium('João', 'joao@gmail.com', 02.02)