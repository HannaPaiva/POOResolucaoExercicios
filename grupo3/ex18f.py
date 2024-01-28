from ex18d import Empregado

class Operario(Empregado):
    def __init__(self, nome='', endereco='', telefone='', codigo_setor='', salario_base=0, imposto=0, valor_producao=0, comissao=0):
        super().__init__(nome, endereco, telefone, codigo_setor, salario_base, imposto)
        self.__valor_producao = valor_producao
        self.__comissao = comissao
        
    def __repr__(self):
        return (f"Operario(nome='{self.get_nome()}', endereco='{self.get_endereco()}', telefone='{self.get_telefone()}', "
                f"codigo_setor='{self.get_codigo_setor()}', salario_base={self.get_salario_base()}, imposto={self.get_imposto()}, "
                f"valor_producao={self.__valor_producao}, comissao={self.__comissao})")
    # Getters
    def get_valor_producao(self):
        return self.__valor_producao

    def get_comissao(self):
        return self.__comissao

    # Setters
    def set_valor_producao(self, valor_producao):
        self.__valor_producao = valor_producao

    def set_comissao(self, comissao):
        self.__comissao = comissao

    # Redefinindo o método calcular_salario
    def calcular_salario(self):
        salario_base_empregado = super().calcular_salario()
        salario_operario = salario_base_empregado + (self.__valor_producao * (self.__comissao / 100))
        return salario_operario

# Programa de teste
operario1 = Operario(nome="Operario1", endereco="Rua XYZ", telefone="987654321", codigo_setor="001", salario_base=3000, imposto=10, valor_producao=5000, comissao=5)
print("Nome:", operario1.get_nome())
print("Endereço:", operario1.get_endereco())
print("Telefone:", operario1.get_telefone())
print("Código Setor:", operario1.get_codigo_setor())
print("Salário Base:", operario1.get_salario_base())
print("Imposto (%):", operario1.get_imposto())
print("Valor Produção:", operario1.get_valor_producao())
print("Comissão (%):", operario1.get_comissao())
print("Salário Operário:", operario1.calcular_salario())
