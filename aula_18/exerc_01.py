class ContaBancaria:
    def __init__(self, saldo: float):
        self.__saldo = 0

    def depositar(self, valor: float):
        self.__saldo += valor

    def sacar(self, valor: float):
        if __saldo >= 0:
            self.sacar -= valor
        else:
            print('Saldo insuficiente')

    def verificar_saldo(self):
        self.__verificar_saldo = saldo

conta1 = ContaBancaria()
conta1.__saldo = 100000
