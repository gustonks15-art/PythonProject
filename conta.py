class Conta:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def investir_poupanca(self, valor):
        self.saldo += valor