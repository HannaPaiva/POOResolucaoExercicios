from flask import Flask, request
import sqlalchemy as sa
import sqlalchemy.orm as sa_orm
import models
import json

app = Flask(__name__)

Base = sa_orm.declarative_base()

def get_session():
    url = 'sqlite:///sensors.db'
    engine = sa.create_engine(url)
    Base.metadata.create_all(engine)
    return sa_orm.sessionmaker(bind=engine)()


#################################################################

# Tabela Alert

@app.route("/alerts", methods=["GET"])
def get_alerts():
    with get_session() as session:
        alerts = session.query(models.Alert)
        return json.dumps(
            [alert.toDict() for alert in alerts]
        )


# Obter informação solicitada através do id
@app.route("/alerts/<id>", methods=["GET"])
def get_alert(id: int):
    with get_session() as session:
        alert = session.get(models.Alert, id)
        if alert == None:
            return '{"Erro" : "Alerta não encontrado"}', 404
        return json.dumps(
            alert.toDict()
        )


@app.route("/alerts", methods=["POST"])
def post_alert():
    with get_session() as session:
        print("ola estou aqui")
        alert = models.Alert.fromDict(request.get_json())
        session.add(alert)
        session.commit()
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route("/alerts/<id>", methods=["PUT"])
def put_alert(id: int):
    with get_session() as session:
        alert = models.Alert.fromDict(request.get_json() | {"unit": id})
        # Operador de união
        # Equivalente ao  comando SQL SELECT * FROM Alert UNION
        session.merge(alert)
        session.commit()
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route("/alerts/<id>", methods=["DELETE"])
def delete_alert(id: int):
    with get_session() as session:
        alert = session.get(models.Alert, id)
        session.delete(alert)
        session.commit()
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


# Tabela Unit


@app.route("/units", methods=["GET"])
def get_units():
    with get_session() as session:
        units = session.query(models.Unit)
        return json.dumps(
            [unit.toDict() for unit in units]
        )


@app.route("/units/<id>", methods=["GET"])
def get_unit(id: int):
    with get_session() as session:
        unit = session.get(models.Unit, id)
        if unit == None:
            return '{"Erro" : "Unidade não encontrada"}', 404
        return json.dumps(
            unit.toDict()
        )


@app.route("/units", methods=["POST"])
def post_unit():
    with get_session() as session:
        unit = models.Unit.fromDict(request.get_json())
        session.add(unit)
        session.commit()
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route("/units/<unit>", methods=["PUT"])
def put_unit(unit: str):
    with get_session() as session:
        unit = models.Unit.fromDict(request.get_json() | {"unit": unit})
        # Operador de união
        session.merge(unit)
        session.commit()
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route("/units/<unit>", methods=["DELETE"])
def delete_unit(unit: str):
    with get_session() as session:
        unit = session.get(models.Unit, unit)
        session.delete(unit)
        session.commit()
        return json.dumps({'Sucesso': True}), 200, {'ContentType': 'application/json'}


# Tabela Location


@app.route("/locations", methods=["GET"])
def get_locations():
    with get_session() as session:
        locations = session.query(models.Location)
        return json.dumps(
            [location.toDict() for location in locations]
        )


@app.route("/locations/<id>", methods=["GET"])
def get_location(id: int):
    with get_session() as session:
        location = session.get(models.Location, id)
        if location == None:
            return '{"Erro" : "Localização não encontrada"}', 404
        return json.dumps(
            location.toDict()
        )


@app.route("/locations", methods=["POST"])
def post_location():
    with get_session() as session:
        location = models.Location.fromDict(request.get_json())
        session.add(location)
        session.commit()
        return json.dumps({'Sucesso': True}), 200, {'ContentType': 'application/json'}


@app.route("/locations/<id>/<name>", methods=["PUT"])
def put_location(id: int, name: str):
    with get_session() as session:
        data = session.get(models.Location, id)
        data.name = name
        print(data)
        #update({"name": "Olhao"})
        #session.merge(data)
        session.commit()
        return json.dumps({'Sucesso': True}), 200, {'ContentType': 'application/json'}


@app.route("/locations/<id>", methods=["DELETE"])
def delete_location(id: int):
    with get_session() as session:
        location = session.get(models.Location, id)
        session.delete(location)
        session.commit()
        return json.dumps({'Sucesso': True}), 200, {'ContentType': 'application/json'}


# Tabela Sensor


@app.route("/sensors", methods=["GET"])
def get_sensors():
    with get_session() as session:
        sensors = session.query(models.Sensor)
        return json.dumps(
            [sensor.toDict() for sensor in sensors]
        )


@app.route("/sensors/<id>", methods=["GET"])
def get_sensor(id: int):
    with get_session() as session:
        sensor = session.get(models.Sensor, id)
        if sensor == None:
            return '{"Erro" : "Sensor não encontrado"}', 404
        return json.dumps(
            sensor.toDict()
        )


@app.route("/sensors", methods=["POST"])
def post_sensor():
    with get_session() as session:
        sensor = models.Sensor.fromDict(request.get_json())
        session.add(sensor)
        session.commit()
        return json.dumps({'Sucesso': True}), 200, {'ContentType': 'application/json'}


@app.route("/sensors/<id>", methods=["PUT"])
def put_sensor(id: int):
    with get_session() as session:
        sensor = models.Sensor.fromDict(request.get_json() | {"id": id})
        # Operador de união
        session.merge(sensor)
        session.commit()
        return json.dumps({'Sucesso': True}), 200, {'ContentType': 'application/json'}


@app.route("/sensors/<id>", methods=["DELETE"])
def delete_sensor(id: int):
    with get_session() as session:
        sensor = session.get(models.Sensor, id)
        session.delete(sensor)
        session.commit()
        return json.dumps({'Sucesso': True}), 200, {'ContentType': 'application/json'}


# Tabela Reading


@app.route("/readings", methods=["GET"])
def get_readings():
    with get_session() as session:
        readings = session.query(models.Reading)
        return json.dumps(
            [reading.toDict() for reading in readings]
        )


@app.route("/readings/<idReading>", methods=["GET"])
def get_reading(idReading: int):
    with get_session() as session:
        reading = session.get(models.Reading, idReading)
        if reading == None:
            return '{"Erro" : "Leitura não encontrada"}', 404
        return json.dumps(
            reading.toDict()
        )


@app.route("/readings", methods=["POST"])
def post_reading():
    with get_session() as session:
        reading = models.Reading.fromDict(request.get_json())
        session.add(reading)
        session.commit()
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route("/readings/<id>", methods=["PUT"])
def put_reading(id: int):
    with get_session() as session:
        reading = models.Reading.fromDict(request.get_json() | {"id": id})
        # Operador de união
        session.merge(reading)
        session.commit()
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route("/readings/<id>", methods=["DELETE"])
def delete_reading(id: int):
    with get_session() as session:
        reading = session.get(models.Reading, id)
        session.delete(reading)
        session.commit()
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


#if __name__ == '__main__':
#  app.run(debug=True)
