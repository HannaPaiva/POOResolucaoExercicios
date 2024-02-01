from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

Base = declarative_base()

class Reading(Base):
    __tablename__ = 'reading'
    idReading = Column(Integer, primary_key=True)
    idSensor = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)
    value = Column(Float)

# Criar o banco de dados e as tabelas
engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)

# Métodos CRUD
@app.route('/readings', methods=['GET'])
def get_readings():
    readings = db.session.query(Reading).all()
    readings_list = []
    for reading in readings:
        readings_list.append({
            'idReading': reading.idReading,
            'idSensor': reading.idSensor,
            'timestamp': reading.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'value': reading.value
        })
    return jsonify({'readings': readings_list})

@app.route('/readings/<int:id>', methods=['GET'])
def get_reading(id):
    reading = db.session.query(Reading).filter_by(idReading=id).first()
    if reading:
        return jsonify({
            'idReading': reading.idReading,
            'idSensor': reading.idSensor,
            'timestamp': reading.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'value': reading.value
        })
    else:
        return jsonify({'message': 'Reading not found'}), 404

@app.route('/readings', methods=['POST'])
def create_reading():
    data = request.get_json()
    new_reading = Reading(idSensor=data['idSensor'], value=data['value'])
    db.session.add(new_reading)
    db.session.commit()
    return jsonify({'message': 'Reading created successfully'}), 201

@app.route('/readings/<int:id>', methods=['PUT'])
def update_reading(id):
    reading = db.session.query(Reading).filter_by(idReading=id).first()
    if reading:
        data = request.get_json()
        reading.idSensor = data['idSensor']
        reading.value = data['value']
        db.session.commit()
        return jsonify({'message': 'Reading updated successfully'})
    else:
        return jsonify({'message': 'Reading not found'}), 404

@app.route('/readings/<int:id>', methods=['DELETE'])
def delete_reading(id):
    reading = db.session.query(Reading).filter_by(idReading=id).first()
    if reading:
        db.session.delete(reading)
        db.session.commit()
        return jsonify({'message': 'Reading deleted successfully'})
    else:
        return jsonify({'message': 'Reading not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
