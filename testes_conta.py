import unittest
from unittest.mock import Mock
from conta import Conta


class TestContaBancaria(unittest.TestCase):

    def test_investimento_poupanca_deve_aumentar_saldo(self):
        minha_conta = Conta(saldo_inicial=100.0)
        valor_investimento = 50.0
        minha_conta.investir_poupanca(valor_investimento)
        self.assertEqual(minha_conta.saldo, 150.0)

    def test_solicitar_cartao_com_doubles(self):
        minha_conta = Conta(saldo_inicial=100.0)

        dummy_usuario = Mock()

        stub_api = Mock()
        stub_api.verificar_limite.return_value = True
        mock_sms = Mock()
        resultado = minha_conta.solicitar_cartao(dummy_usuario, stub_api, mock_sms)

        self.assertEqual(resultado, "Cartão Aprovado")

        mock_sms.enviar_sms.assert_called_once()


if __name__ == '__main__':
    unittest.main()

# EXERCÍCIO 7.5 - TDD
def test_rendimento_poupanca(self):
    minha_conta = Conta(saldo_inicial=1000.0)

       minha_conta.calcular_rendimento()

        self.assertEqual(minha_conta.saldo, 1005.0)