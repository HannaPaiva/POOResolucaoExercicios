from ex18b import Pessoa

class Empregado(Pessoa):
    def __init__(self, nome='', endereco='', telefone='', codigo_setor='', salario_base=0, imposto=0):
        super().__init__(nome, endereco, telefone)
        self.__codigo_setor = codigo_setor
        self.__salario_base = salario_base
        self.__imposto = imposto
        
    def __repr__(self):
        return (f"Empregado(nome='{self.get_nome()}', endereco='{self.get_endereco()}', telefone='{self.get_telefone()}', "
                f"codigo_setor='{self.__codigo_setor}', salario_base={self.__salario_base}, imposto={self.__imposto})")
    # Getters
    def get_codigo_setor(self):
        return self.__codigo_setor

    def get_salario_base(self):
        return self.__salario_base

    def get_imposto(self):
        return self.__imposto

    # Setters
    def set_codigo_setor(self, codigo_setor):
        self.__codigo_setor = codigo_setor

    def set_salario_base(self, salario_base):
        self.__salario_base = salario_base

    def set_imposto(self, imposto):
        self.__imposto = imposto

    def calcular_salario(self):
        salario_liquido = self.__salario_base - (self.__salario_base * (self.__imposto / 100))
        return salario_liquido

# Programa de teste
empregado1 = Empregado(nome="Empregado1", endereco="Rua XYZ", telefone="987654321", codigo_setor="001", salario_base=3000, imposto=10)
print("Nome:", empregado1.get_nome())
print("Endereço:", empregado1.get_endereco())
print("Telefone:", empregado1.get_telefone())
print("Código Setor:", empregado1.get_codigo_setor())
print("Salário Base:", empregado1.get_salario_base())
print("Imposto (%):", empregado1.get_imposto())
print("Salário Líquido:", empregado1.calcular_salario())
