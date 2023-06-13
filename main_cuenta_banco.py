from cuenta_banco import (
    CajaAhorro,
    SaldoInsuficiente,
    CuentaCorriente,
)


def main():
    caja_ahorro = CajaAhorro()
    cuenta_corriente = CuentaCorriente()
    while True:
        tipo_cuenta = input('Ingrese tipo cuenta: (A/C) o Q para salir')
        if tipo_cuenta == 'Q':
            break
        elif tipo_cuenta == 'C':
            cuenta = cuenta_corriente
        else:
            cuenta = caja_ahorro
        tipo_operacion = input('Ingrese tipo operacion: (C/D/R)')
        if tipo_operacion != 'C':
            while True:
                try:
                    monto = int(input('Ingrese monto: '))
                    break
                except Exception as e:
                    print('ingrese un valor positivo')
        if tipo_operacion == 'D':
            cuenta.deposito(monto)
        elif tipo_operacion == 'R':
            try:
                cuenta.retiro(monto)
            except SaldoInsuficiente as e:
                print(e)
            except ExcedeDescubiertoException as e:
                print(e)
            except Exception as e:
                print(e)
        print('El saldo de la cuenta es: ' + str(cuenta.saldo) )


if __name__ == '__main__':
    main()