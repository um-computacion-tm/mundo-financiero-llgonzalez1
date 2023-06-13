class SaldoInsuficiente(Exception):
    pass


class CajaAhorro:

    def __init__(self):
        self.saldo = 0

    def deposito(self, monto):
        self.saldo += monto

    def retiro(self, monto):
        if monto > self.saldo:
            raise SaldoInsuficiente()
        self.saldo -= monto
