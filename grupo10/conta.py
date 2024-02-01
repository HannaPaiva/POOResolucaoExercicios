class Conta:

    def __init__(self, dono, taxa_de_juro=0, saldo=0):
        self._dono = dono
        self._taxa_de_juro = max(0, taxa_de_juro)
        self._saldo = max(0, saldo)

    @property
    def dono(self):
        """Devolve o dono formatado."""
        return self._dono.title()

    @dono.setter
    def dono(self, value):
        """Guarda uma string formatada em "title"."""
        self._dono = value.title()

    @property
    def taxa_de_juro(self):
        """Devolve a taxa de juro."""
        return self._taxa_de_juro

    @taxa_de_juro.setter
    def taxa_de_juro(self, value):
        """Guarda a taxa de juro."""
        self._taxa_de_juro = max(0, float(value))

    @property
    def saldo(self):
        """Devolve o saldo."""
        return self._saldo

    @saldo.setter
    def saldo(self, value):
        """Guarda o saldo."""
        self._saldo = max(0, float(value))

    def capitaliza(self):
        """Acrescenta os juros ao saldo."""
        juros = self._saldo * (self._taxa_de_juro / 100)
        self._saldo += juros

    def cobra_comissao(self, comissao):
        """Retira o valor da comissão ao saldo."""
        cobrado = min(comissao, self._saldo)
        self._saldo -= cobrado
        return cobrado

    def faz_levantamento(self, valor):
        """Subtrai ao saldo o valor desde que o saldo se mantenha positivo."""
        if valor <= self._saldo:
            self._saldo -= valor
            return True
        else:
            return False

    def faz_deposito(self, valor):
        """Acrescenta ao saldo o valor."""
        self._saldo += valor


# Exemplo de uso
if __name__ == '__main__':
    conta_exemplo = Conta("Maicon Douglas", 2, 1000)
    print(f"Saldo antes da capitalização: {conta_exemplo.saldo}")
    conta_exemplo.capitaliza()
    print(f"Saldo após a capitalização: {conta_exemplo.saldo}")

    comissao_cobrada = conta_exemplo.cobra_comissao(10)
    print(f"Comissão cobrada: {comissao_cobrada}")
    print(f"Saldo após a cobrança de comissão: {conta_exemplo.saldo}")

    levantamento_feito = conta_exemplo.faz_levantamento(200)
    print(f"Levantamento feito: {levantamento_feito}")
    print(f"Saldo após o levantamento: {conta_exemplo.saldo}")

    conta_exemplo.faz_deposito(500)
    print(f"Saldo após o depósito: {conta_exemplo.saldo}")
