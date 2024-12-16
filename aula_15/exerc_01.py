class Elevador:
    def __init__(self, total_pisos: int):
        self.piso_atual = 0
        self.total_pisos = total_pisos
        
        
    def subir(self, qtd_andares: int):
        andar_final = self.piso_atual + qtd_andares
        if andar_final > self.total_pisos:
            print('Não é possível subir')
        else:
            self.piso_atual = andar_final
            
    def descer(self, ):

elevador1 = Elevador(10)
print(elevador1.piso_atual)
elevador1.subir(6)
print(elevador1.piso_atual)
elevador1.subir(2)
print(elevador1.piso_atual)
elevador1.subir(3)
print(elevador1.piso_atual)