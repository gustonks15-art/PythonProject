
class Conta:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def investir_poupanca(self, valor):
        self.saldo += valor

    def solicitar_cartao(self, usuario, api_credito, servico_notificacao):
        # A api_credito e o servico_notificacao são dependências externas!
        if api_credito.verificar_limite():
            servico_notificacao.enviar_sms()
            return "Cartão Aprovado"
        return "Cartão Negado"