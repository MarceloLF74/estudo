class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo

    def depositar(self, valor):
        self.depositar += valor

    def sacar(self, valor):
        if __saldo > 0:
            self.sacar -= valor
        else:
            print('Saldo insuficiente')

    def verificar_saldo(self, saldo):
        self.__verificar_saldo = saldo


saldo = 0


