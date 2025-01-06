class Produto:
    def __init__(self, nome: str, preco: float, cor: str, qnt_estoque: int):
        self.nome = nome
        self.preco = preco
        self.cor = cor
        self.qnt_estoque = qnt_estoque


class CarrinhoDeCompras:
    def __init__(self):
        self.lista_produtos = []
   
    def adicionar_produto(self, produto: Produto):
        self.lista_produtos.append(produto)


    def visualizar_produtos(self):
        print('lista de produtos do carrinho:')
        if self.lista_produtos != []:
            for produto in self.lista_produtos:
                print(produto.nome)


    def calcular_preco_total(self):
        soma = 0
        for produto in self.lista_produtos:
            soma += produto.preco
        print(f'O total é: R$ {soma}')


produto_1 = Produto('Relógio', 15000, 'Prata', 1)
produto_2 = Produto('Blusa', 30, 'Preta', 100)
produto_3 = Produto('Tênis', 230, 'Vermelho', 300)




lista = [produto_2.nome]




carrinho_1 = CarrinhoDeCompras()
print(f'Antes: {carrinho_1.lista_produtos}')
carrinho_1.adicionar_produto(produto_2)
carrinho_1.adicionar_produto(produto_2)
carrinho_1.adicionar_produto(produto_3)
carrinho_1.visualizar_produtos()
carrinho_1.calcular_preco_total()
