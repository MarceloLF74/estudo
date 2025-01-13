class Personagem:
    def __init__(self, nome: str, poder: str, ataque: int, defesa: int, vida: int):
        self.nome = nome
        self.poder = poder
        self.ataque = ataque
        self.defesa = defesa
        self.vida = vida
   
    def atacar(self, personagem):
        dano = self.ataque - personagem.defesa
        personagem.vida -= dano
        print(f'{self.nome} atacou {personagem.nome} com {self.poder} e tirou {dano}')


class Heroi(Personagem):    
    def __init__(self, nome: str, poder: str, ataque: int, defesa: int, vida: int):
        super().__init__(nome, poder, ataque, defesa, vida)


    def comer_maca(self):
        self.vida += 10


class Vilao(Personagem):
    def __init__(self, nome: str, poder: str, ataque: int, defesa: int, vida: int):
        super().__init__(nome, poder, ataque, defesa, vida)






heroi_1 = Heroi('Topetudo', 'Soltar fogo', 10, 3, 80)
vilao_1 = Vilao('Mun-ha', 'Magia negra', 5, 8, 120)
heroi_1.atacar(vilao_1)
print(f'Vida do {vilao_1.nome} após ataque: {vilao_1.vida}')
vilao_1.atacar(heroi_1)
print(f'Vida do {heroi_1.nome} após ataque: {heroi_1.vida}')
vilao_1.atacar(heroi_1)
print(f'Vida do {heroi_1.nome} após ataque: {heroi_1.vida}')





