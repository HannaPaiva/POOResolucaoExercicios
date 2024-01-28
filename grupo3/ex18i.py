from ex18d import Empregado

class Vendedor(Empregado):
    def __init__(self, nome='', endereco='', telefone='', codigo_setor='', salario_base=0, imposto=0, valor_vendas=0, comissao=0):
        super().__init__(nome, endereco, telefone, codigo_setor, salario_base, imposto)
        self.__valor_vendas = valor_vendas
        self.__comissao = comissao
        
    def __repr__(self):
        return (f"Vendedor(nome='{self.get_nome()}', endereco='{self.get_endereco()}', telefone='{self.get_telefone()}', "
                f"codigo_setor='{self.get_codigo_setor()}', salario_base={self.get_salario_base()}, imposto={self.get_imposto()}, "
                f"valor_vendas={self.__valor_vendas}, comissao={self.__comissao})")
    # Getters
    def get_valor_vendas(self):
        return self.__valor_vendas

    def get_comissao(self):
        return self.__comissao

    # Setters
    def set_valor_vendas(self, valor_vendas):
        self.__valor_vendas = valor_vendas

    def set_comissao(self, comissao):
        self.__comissao = comissao

    # Redefinindo o método calcular_salario
    def calcular_salario(self):
        salario_base_empregado = super().calcular_salario()
        salario_vendedor = salario_base_empregado + (self.__valor_vendas * (self.__comissao / 100))
        return salario_vendedor

# Programa de teste
vendedor1 = Vendedor(nome="Vendedor1", endereco="Rua XYZ", telefone="987654321", codigo_setor="001", salario_base=3000, imposto=10, valor_vendas=10000, comissao=3)
print("Nome:", vendedor1.get_nome())
print("Endereço:", vendedor1.get_endereco())
print("Telefone:", vendedor1.get_telefone())
print("Código Setor:", vendedor1.get_codigo_setor())
print("Salário Base:", vendedor1.get_salario_base())
print("Imposto (%):", vendedor1.get_imposto())
print("Valor Vendas:", vendedor1.get_valor_vendas())
print("Comissão (%):", vendedor1.get_comissao())
print("Salário Vendedor:", vendedor1.calcular_salario())
