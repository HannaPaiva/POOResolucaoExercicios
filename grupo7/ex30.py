import mysql.connector

config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'adamastor'
}

class Adamastor:
    def __init__(self, config):
        self.cnx = mysql.connector.connect(**config)
        self.cursor = self.cnx.cursor(dictionary=True)
    
    def listar_clientes(self):
        sql = 'SELECT * FROM clientes limit 2'
        self.cursor.execute(sql)
        return self.cursor.fetchall()
        
    def listar_clientes_da_cidade(self, cidade):
        sql = 'SELECT * FROM clientes WHERE cidade = %s limit 2'
        self.cursor.execute(sql, (cidade,))
        return self.cursor.fetchall()

    def listar_encomendas_entre_datas(self, data_inicial, data_final):
        sql = 'SELECT * FROM encomendas WHERE DataDaEncomenda BETWEEN %s AND %s ORDER BY CódigoDoCliente limit 2'
        self.cursor.execute(sql, (data_inicial, data_final))
        return self.cursor.fetchall()

    def listar_datas_encomendas_cliente(self, id_cliente):
        sql = 'SELECT DataDaEncomenda FROM encomendas WHERE CódigoDoCliente = %s limit 2'
        self.cursor.execute(sql, (id_cliente,))
        return [item['DataDaEncomenda'] for item in self.cursor.fetchall()]

    def inserir_novo_produto(self, nome_produto, codigo_fornecedor, codigo_categoria, quantidade_por_unidade, preco_unitario, existencias, unidades_encomendadas, existencia_minima, descontinuado):
        sql = 'INSERT INTO produtos (NomeDoProduto, CódigoDoFornecedor, CódigoDaCategoria, QuantidadePorUnidade, PreçoUnitário, Existências, UnidadesEncomendadas, ExistênciaMínima, Descontinuado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
        values = (nome_produto, codigo_fornecedor, codigo_categoria, quantidade_por_unidade, preco_unitario, existencias, unidades_encomendadas, existencia_minima, descontinuado)
        self.cursor.execute(sql, values)
        self.cnx.commit()
        return self.cursor.lastrowid

    def preco_minimo_produto(self):
        sql = 'SELECT MIN(PreçoUnitário) AS PreçoMínimo FROM produtos limit 2'
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        return result['PreçoMínimo']

    def fornecedores_por_cidade(self, cidade):
        sql = 'SELECT DISTINCT NomeDaEmpresa FROM fornecedores WHERE Cidade = %s limit 2'
        self.cursor.execute(sql, (cidade,))
        return [item['NomeDaEmpresa'] for item in self.cursor.fetchall()]

    def maior_encomenda_valor(self):
        sql = 'SELECT CódigoDaEncomenda, SUM(PreçoUnitário * Quantidade) AS ValorTotal FROM detalhes_da_encomenda GROUP BY CódigoDaEncomenda ORDER BY ValorTotal DESC LIMIT 1'
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        return result['CódigoDaEncomenda'], result['ValorTotal']

adam = Adamastor(config)

print("Listar clientes:".center(80, "."))
clientes = adam.listar_clientes()
for cliente in clientes:
    print(cliente)

print("\nListar clientes da cidade:".center(80, "."))
clientes_cidade = adam.listar_clientes_da_cidade("Lisboa")
for cliente in clientes_cidade:
    print(cliente)

print("\nListagem de encomendas entre 10-7-1996 e 17-7-1996 ordenadas por id do cliente:".center(80, "."))
encomendas_entre_datas = adam.listar_encomendas_entre_datas('1996-07-10', '1996-07-17')
for encomenda in encomendas_entre_datas:
    print(encomenda)

print("\nListagem das datas de encomendas de um cliente:".center(80, "."))
datas_encomendas_cliente = adam.listar_datas_encomendas_cliente('ALFKI')
print(datas_encomendas_cliente)

print("\nInserir um novo produto:".center(80, "."))



codigo_fornecedor = 1

codigo_categoria = 1

novo_produto_id = adam.inserir_novo_produto('Novo Produto', codigo_fornecedor, codigo_categoria, '1 unidade', 10.99, 100, 0, 10, 0)
print("Novo produto inserido com ID:", novo_produto_id)

print("\nPreço mínimo entre todos os produtos:".center(80, "."))
preco_minimo = adam.preco_minimo_produto()
print("Preço mínimo:", preco_minimo)

print("\nFornecedores de uma cidade:".center(80, "."))
fornecedores_cidade = adam.fornecedores_por_cidade('Paris')
print(fornecedores_cidade)

print("\nMaior encomenda em termos de valor:".center(80, "."))
codigo_encomenda, valor_total = adam.maior_encomenda_valor()
print("Código da encomenda:", codigo_encomenda)
print("Valor total da encomenda:", valor_total)

adam.cursor.close()
adam.cnx.close()
