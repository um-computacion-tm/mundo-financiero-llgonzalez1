import unittest

from L_cuenta_banco import ( CajaAhorro, MontoIngresadoInvalido
    #SaldoInsuficiente,
)


class TestCajaAhorro(unittest.TestCase):

    def test_inicio_caja_ahorro(self):
        caja_ahorro = CajaAhorro()
        self.assertEqual(
            caja_ahorro.saldo,
            0,
        )

    def test_deposito_caja_ahorro(self):
        caja_ahorro = CajaAhorro()
        caja_ahorro.deposito(100)
        self.assertEqual(
            caja_ahorro.saldo,
            100,
        )

    def test_segundo_deposito_caja_ahorro(self):
        caja_ahorro = CajaAhorro()
        caja_ahorro.deposito(100)
        caja_ahorro.deposito(1000)
        self.assertEqual(
            caja_ahorro.saldo,
            1100,
        )
    
    def test_deposito_dos_cajas_ahorro(self):
        caja_ahorro = CajaAhorro()
        caja_ahorro_2 = CajaAhorro()
        caja_ahorro.deposito(100)
        caja_ahorro_2.deposito(200)
        self.assertEqual(
            caja_ahorro.saldo,
            100,
        )
        self.assertEqual(
            caja_ahorro_2.saldo,
             200,
        )

#    def test_retiro_cajas_ahorro(self):
#        caja_ahorro = CajaAhorro()
#        caja_ahorro.deposito(100)
#        caja_ahorro.retiro(80)
#        self.assertEqual(
#            caja_ahorro.saldo,
#            20,
#        )
#
#    def test_retiro_cajas_ahorro_sin_saldo(self):
#        caja_ahorro = CajaAhorro()
#        with self.assertRaises(SaldoInsuficiente):
#            caja_ahorro.retiro(80)
#        self.assertEqual(
#            caja_ahorro.saldo,
#            0,
#        )
#
#
if __name__ == '__main__':
    unittest.main()