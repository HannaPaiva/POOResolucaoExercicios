from flask import Flask, request
from flask_restful import Api, Resource, reqparse
import sqlite3
from datetime import datetime

app = Flask(__name__)
api = Api(app)

# Configurando o parser para os argumentos da API
parser_cliente = reqparse.RequestParser()
parser_cliente.add_argument('nome')
parser_cliente.add_argument('morada')
parser_cliente.add_argument('telefone')

parser_pizza = reqparse.RequestParser()
parser_pizza.add_argument('nome')
parser_pizza.add_argument('ingredientes')

parser_encomenda = reqparse.RequestParser()
parser_encomenda.add_argument('id_cliente')
parser_encomenda.add_argument('id_pizza')
parser_encomenda.add_argument('quantidade')
parser_encomenda.add_argument('tamanho')
parser_encomenda.add_argument('data_hora')

class ClienteResource(Resource):
    def get(self):
        connection = sqlite3.connect('pizzaria.sqlite')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Clientes')
        clientes = [{'id_cliente': row[0], 'nome': row[1], 'morada': row[2], 'telefone': row[3]} for row in cursor.fetchall()]
        connection.close()
        return clientes

    def post(self):
        args = parser_cliente.parse_args()

        nome = args['nome']
        morada = args['morada']
        telefone = args['telefone']

        # Inserir dados na tabela Clientes
        connection = sqlite3.connect('pizzaria.sqlite')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO Clientes (nome, morada, telefone) VALUES (?, ?, ?)', (nome, morada, telefone))
        connection.commit()
        connection.close()

        return {'message': 'Cliente adicionado com sucesso'}, 201

class PizzaResource(Resource):
    def get(self):
        connection = sqlite3.connect('pizzaria.sqlite')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Pizzas')
        pizzas = [{'id_pizza': row[0], 'nome': row[1], 'ingredientes': row[2]} for row in cursor.fetchall()]
        connection.close()
        return pizzas

    def post(self):
        args = parser_pizza.parse_args()

        nome = args['nome']
        ingredientes = args['ingredientes']

        # Inserir dados na tabela Pizzas
        connection = sqlite3.connect('pizzaria.sqlite')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO Pizzas (nome, ingredientes) VALUES (?, ?)', (nome, ingredientes))
        connection.commit()
        connection.close()

        return {'message': 'Pizza adicionada com sucesso'}, 201

class EncomendaResource(Resource):
    def get(self):
        connection = sqlite3.connect('pizzaria.sqlite')
        cursor = connection.cursor()

        # Consulta para obter dados da tabela Encomendas com informações adicionais
        cursor.execute('''
            SELECT E.*, C.nome AS cliente_nome, P.nome AS pizza_nome
            FROM Encomendas E
            LEFT JOIN Clientes C ON E.id_cliente = C.id_cliente
            LEFT JOIN Pizzas P ON E.id_pizza = P.id_pizza
            ORDER BY e.id_encomenda DESC
        ''')

        encomendas = []
        for row in cursor.fetchall():
            encomenda = {
                'id_encomenda': row[0],
                'id_cliente': row[1],
                'id_pizza': row[2],
                'quantidade': row[3],
                'tamanho': row[4],
                'data_hora': row[5],
                'cliente_nome': row[6],
                'pizza_nome': row[7]
            }
            encomendas.append(encomenda)

        connection.close()
        return encomendas

    def post(self):
        args = parser_encomenda.parse_args()

        id_cliente = args['id_cliente']
        id_pizza = args['id_pizza']
        quantidade = args['quantidade']
        tamanho = args['tamanho']
        data_hora = args['data_hora'] or datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Inserir dados na tabela Encomendas
        connection = sqlite3.connect('pizzaria.sqlite')
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO Encomendas (id_cliente, id_pizza, quantidade, tamanho, data_hora)
            VALUES (?, ?, ?, ?, ?)
        ''', (id_cliente, id_pizza, quantidade, tamanho, data_hora))

        connection.commit()
        connection.close()

        return {'message': 'Encomenda adicionada com sucesso'}, 201

api.add_resource(ClienteResource, '/clientes')
api.add_resource(PizzaResource, '/pizzas')
api.add_resource(EncomendaResource, '/encomendas')

if __name__ == '__main__':
    app.run(debug=True)
