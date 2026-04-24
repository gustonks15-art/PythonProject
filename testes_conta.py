import unittest
from conta import Conta


class TestContaBancaria(unittest.TestCase):

    def test_investimento_poupanca_deve_aumentar_saldo(self):
        minha_conta = Conta(saldo_inicial=100.0)
        valor_investimento = 50.0

        minha_conta.investir_poupanca(valor_investimento)

        self.assertEqual(minha_conta.saldo, 150.0)


if __name__ == '__main__':
    unittest.main()