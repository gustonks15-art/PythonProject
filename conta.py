class Conta:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def investir_poupanca(self, valor):
        self.saldo += valor

    def solicitar_cartao(self, usuario, api_credito, servico_notificacao):
        if api_credito.verificar_limite():
            servico_notificacao.enviar_sms()
            return "Cartão Aprovado"
        return "Cartão Negado"


    def calcular_rendimento(self):
        rendimento = self.saldo * 0.005
        self.saldo += rendimento