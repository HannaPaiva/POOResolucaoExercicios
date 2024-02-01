from ex18b import Pessoa

class Fornecedor(Pessoa):
    def __init__(self, nome='', endereco='', telefone='', valor_credito=0, valor_divida=0):
        super().__init__(nome, endereco, telefone)
        self.__valor_credito = valor_credito
        self.__valor_divida = valor_divida


    def __repr__(self):
        return (f"Fornecedor(nome='{self.get_nome()}', endereco='{self.get_endereco()}', telefone='{self.get_telefone()}', "
                f"valor_credito={self.__valor_credito}, valor_divida={self.__valor_divida})")
    
   
    def get_valor_credito(self):
        return self.__valor_credito

    def get_valor_divida(self):
        return self.__valor_divida


    def set_valor_credito(self, valor_credito):
        self.__valor_credito = valor_credito

    def set_valor_divida(self, valor_divida):
        self.__valor_divida = valor_divida

    def obter_saldo(self):
        return self.__valor_credito - self.__valor_divida

# Programa de teste
fornecedor1 = Fornecedor(nome="Fornecedor1", endereco="Rua XYZ", telefone="987654321", valor_credito=5000, valor_divida=2000)
print("Nome:", fornecedor1.get_nome())
print("Endereço:", fornecedor1.get_endereco())
print("Telefone:", fornecedor1.get_telefone())
print("Valor de Crédito:", fornecedor1.get_valor_credito())
print("Valor de Dívida:", fornecedor1.get_valor_divida())
print("Saldo:", fornecedor1.obter_saldo())
