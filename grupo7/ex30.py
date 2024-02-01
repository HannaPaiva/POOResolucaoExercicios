import mysql.connector

config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'adamastor'
}

def execute_query(query, params=None):
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        result = cursor.fetchall()
        return result

    except Exception as e:
        print(f"Erro ao executar a query: {e}")

    finally:
        cursor.close()
        connection.close()

# (i) SELECT * FROM produtos ORDER BY PreçoUnitário ASC
def query_i():
    query = "SELECT * FROM produtos ORDER BY PreçoUnitário ASC"
    return execute_query(query)

# (iv) SELECT c.*, p.* FROM categorias c LEFT JOIN produtos p ON c.CódigoDaCategoria = p.códigoDaCategoria WHERE c.`CódigoDaCategoria` = %s
def query_iv(categoria_id):
    query = "SELECT c.*, p.* FROM categorias c LEFT JOIN produtos p ON c.CódigoDaCategoria = p.códigoDaCategoria WHERE c.`CódigoDaCategoria` = %s"
    return execute_query(query, (categoria_id,))

# (x) SELECT * FROM encomendas WHERE datadaencomenda BETWEEN %s AND %s ORDER BY códigoDoCliente
def query_x(data_inicio, data_fim):
    query = "SELECT * FROM encomendas WHERE datadaencomenda BETWEEN %s AND %s ORDER BY códigoDoCliente"
    return execute_query(query, (data_inicio, data_fim))

# (xii) SELECT datadaencomenda FROM encomendas WHERE códigodocliente = %s
def query_xii(codigo_cliente):
    query = "SELECT datadaencomenda FROM encomendas WHERE códigodocliente = %s"
    return execute_query(query, (codigo_cliente,))


def query_xxi():
    query =  "INSERT INTO produtos VALUES (DEFAULT 'Borracha de desenho', 1, 1, 1, 10, 100, 12, 50, 0)"
    execute_query(query)
    print("ok")
    
# (xxvi) SELECT min(preçoUnitário) FROM produtos
def query_xxvi():
    query = "SELECT min(preçoUnitário) FROM produtos"
    return execute_query(query)

# (xxx) SELECT * FROM fornecedores WHERE país = %s
def query_xxx(pais):
    query = "SELECT * FROM fornecedores WHERE país = %s"
    return execute_query(query, (pais,))

# SELECT CódigoDaEncomenda, SUM(PreçoUnitário * Quantidade) AS ValorTotal FROM detalhes_da_encomenda GROUP BY CódigoDaEncomenda ORDER BY ValorTotal DESC LIMIT 1
def query_sum_valor_total():
    query = "SELECT CódigoDaEncomenda, SUM(PreçoUnitário * Quantidade) AS ValorTotal FROM detalhes_da_encomenda GROUP BY CódigoDaEncomenda ORDER BY ValorTotal DESC LIMIT 1"
    return execute_query(query)



if __name__ == "__main__":
    print("(i) SELECT * FROM produtos ORDER BY PreçoUnitário ASC:")
    result_i = query_i()
    print(result_i)
    print("......................................................................")
    print("\n(iv) SELECT c.*, p.* FROM categorias c LEFT JOIN produtos p ON c.CódigoDaCategoria = p.códigoDaCategoria WHERE c.`CódigoDaCategoria` = 2:")
    result_iv = query_iv(1)
    print(result_iv)
    print("......................................................................")

    print("\n(x) SELECT * FROM encomendas WHERE datadaencomenda BETWEEN '1996-07-10' AND '1996-07-17' ORDER BY códigoDoCliente:")
    result_x = query_x('1996-07-10', '1996-07-17')
    print(result_x)
    print("......................................................................")

    print('\n(xii) SELECT datadaencomenda FROM encomendas WHERE códigodocliente = "HANAR":')
    result_xii = query_xii('HANAR')
    print(result_xii)
    print("......................................................................")

    print('\n(xxi) INSERT INTO produtos:')
    query_xxi()
    print("......................................................................")

    print('\n(xxvi) SELECT min(preçoUnitário) FROM produtos:')
    result_xxvi = query_xxvi()
    print(result_xxvi)
    print("......................................................................")

    print('\n(xxx) SELECT * FROM fornecedores WHERE país = "França":')
    result_xxx = query_xxx("França")
    print(result_xxx)
    print("......................................................................")
    print('\nSUM(PreçoUnitário * Quantidade) por CódigoDaEncomenda:')
    result_sum_valor_total = query_sum_valor_total()
    print(result_sum_valor_total)
    print("......................................................................")