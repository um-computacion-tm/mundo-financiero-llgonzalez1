class CuentaBanco:
    def __init__(self):
        self.saldo= 0
        self.deuda= -200
class CajaAhorro(CuentaBanco): 
    def deposito(self, monto):
        self.saldo += monto
    def retiro(self, monto):
        