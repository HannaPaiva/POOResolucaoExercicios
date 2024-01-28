class Pessoa:
    def __init__(self, nome='', endereco='', telefone=''):
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone
        
    def __repr__(self):
        return f"Pessoa(nome='{self.__nome}', endereco='{self.__endereco}', telefone='{self.__telefone}')"
    # Getters
    def get_nome(self):
        return self.__nome

    def get_endereco(self):
        return self.__endereco

    def get_telefone(self):
        return self.__telefone

    # Setters
    def set_nome(self, nome):
        self.__nome = nome

    def set_endereco(self, endereco):
        self.__endereco = endereco

    def set_telefone(self, telefone):
        self.__telefone = telefone

# Exemplo de uso
pessoa1 = Pessoa()
pessoa1.set_nome("João")
pessoa1.set_endereco("Rua ABC, 123")
pessoa1.set_telefone("123456789")

print("Nome:", pessoa1.get_nome())
print("Endereço:", pessoa1.get_endereco())
print("Telefone:", pessoa1.get_telefone())
