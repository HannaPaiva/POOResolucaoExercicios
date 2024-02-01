from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# ookkk
db_config = {
    'host': 'localhost',
    'database': 'sensores',
    'user': 'root',
    'password': ''
}

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            print(f'Conectado ao banco de dados: {db_config["database"]}')
        return connection
    except Error as e:
        print(f'Erro ao conectar ao banco de dados: {e}')
        return None

# Rotas CRUD para a tabela Reading
@app.route('/readings', methods=['GET'])
def get_readings():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute('SELECT * FROM Reading')
            readings = cursor.fetchall()
            return jsonify(readings)
        except Error as e:
            return jsonify({'error': str(e)})
        finally:
            cursor.close()
            connection.close()

@app.route('/readings/<int:reading_id>', methods=['GET'])
def get_reading(reading_id):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute('SELECT * FROM Reading WHERE idReading = %s', (reading_id,))
            reading = cursor.fetchone()
            if reading:
                return jsonify(reading)
            else:
                return jsonify({'error': 'Reading not found'}), 404
        except Error as e:
            return jsonify({'error': str(e)})
        finally:
            cursor.close()
            connection.close()

@app.route('/readings', methods=['POST'])
def create_reading():
    data = request.get_json()
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO Reading VALUES (DEFAULT, %s, %s, %s)',
                           (data['idSensor'], data['timestamp'], data['value']))
            connection.commit()
            return jsonify({'message': 'Reading created successfully'})
        except Error as e:
            return jsonify({'error': str(e)})
        finally:
            cursor.close()
            connection.close()

@app.route('/readings/<int:reading_id>', methods=['PUT'])
def update_reading(reading_id):
    data = request.get_json()
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute('UPDATE Reading SET idSensor = %s, timestamp = %s, value = %s WHERE idReading = %s',
                           (data['idSensor'], data['timestamp'], data['value'], reading_id))
            connection.commit()
            return jsonify({'message': 'Reading updated successfully'})
        except Error as e:
            return jsonify({'error': str(e)})
        finally:
            cursor.close()
            connection.close()

@app.route('/readings/<int:reading_id>', methods=['DELETE'])
def delete_reading(reading_id):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute('DELETE FROM Reading WHERE idReading = %s', (reading_id,))
            connection.commit()
            return jsonify({'message': 'Reading deleted successfully'})
        except Error as e:
            return jsonify({'error': str(e)})
        finally:
            cursor.close()
            connection.close()

if __name__ == '__main__':
    app.run(debug=True)