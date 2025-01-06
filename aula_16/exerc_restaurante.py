class restaurante:
    def __init__(self, nome: str, tipo_cozinha: str, avaliacao_media: float):
        self.nome = nome
        self.tipo_cozinha = tipo_cozinha
        self.avaliacao_media = avaliacao_media

    def mostrar_informacoes(self):
        print(f'Nome do Resturante: {restaurante_1}')
        print(f'Tipo de Cozinha: {restaurante_1}')
        print(f'Avaliação Média: {restaurante_1}')

restaurante_1 = restaurante('Hamburgueria do João', 'Hambúgueres', 4.5)

