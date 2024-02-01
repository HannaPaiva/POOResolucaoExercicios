import mysql.connector
from mysql.connector import Error


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

def show_alert_data():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute('SELECT * FROM Alert')
            alerts = cursor.fetchall()
            
            for alert in alerts:
                
                print('...............................................................')
                print()
                print(f'Alert ID: {alert["idAlert"]}')
                print(f'Sensor ID: {alert["idSensor"]}')
                print(f'Timestamp: {alert["timestamp"]}')
                print(f'Description: {alert["description"]}')
                print(f'Cleared: {alert["cleared"]}')
                print()
                print('...............................................................')

        except Error as e:
            print(f'Erro ao executar a consulta: {e}')
        finally:
            cursor.close()
            connection.close()

if __name__ == '__main__':
    show_alert_data()
