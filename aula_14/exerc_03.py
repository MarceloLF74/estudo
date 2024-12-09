class Produtos:
    def __init__(self, nome:str, preco: int, quantidade: int):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def exibir_informacoes(self):
        print(f'Produto: {self.nome}, Preço: R$ {self.preco}, Quantidade: {self.quantidade}')

produto_1 = Produtos('Smartphone', 1200.00, 10)
produto_2 = Produtos('Notebook', 3500.00, 5)

produto_1.exibir_informacoes()
produto_2.exibir_informacoes()
