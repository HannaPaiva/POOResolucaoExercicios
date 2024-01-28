from datetime import datetime
import random
import sqlalchemy as sa
import sqlalchemy.orm as sa_orm

Base = sa_orm.declarative_base()

class Location(Base):
    __tablename__ = 'Location'

    def __init__(self, id: int, name: str, description: str):
        self.idLocation = id
        self.name = name
        self.description = description

    idLocation = sa.Column(sa.Integer, primary_key = True)
    name = sa.Column(sa.String(45))
    description = sa.Column(sa.String(45))

    def __repr__(self):
        return f"{self.idLocation} : {self.name} ({self.description})"
    
    def toDict(self):
        return {
            "idLocation" : self.idLocation,
            "name" : self.name,
            "description" : self.description
        }

    @staticmethod
    def fromDict(data : dict):
        return Location(data.get("idLocation", None), data["name"], data["description"])

class Unit(Base):
    __tablename__ = 'unit'

    def __init__(self, unit : str, description : str):
        self.unit = unit
        self.description = description
    
    def __repr__(self):
        return f"{self.unit} : {self.description}"

    unit = sa.Column(sa.String(45), primary_key = True)
    description = sa.Column(sa.String(45))

    def toDict(self):
        return {
            "unit": self.unit,
            "description": self.description
        }

    @staticmethod
    def fromDict(data: dict):
        return Unit(data["unit"], data["description"])

class Sensor(Base):
    __tablename__ = 'sensor' 

    def __init__(self, idSensor: int, idLocation : int, name : str, unit : str):
        self.idSensor = idSensor
        self.idLocation = idLocation
        self.name = name
        self.unit = unit

    idSensor = sa.Column(sa.Integer(), primary_key = True)
    idLocation = sa.Column(sa.Integer, sa.ForeignKey(Location.idLocation))
    name = sa.Column(sa.String(45))
    unit = sa.Column(sa.String(45), sa.ForeignKey(Unit.unit))

    def __repr__(self):
        return f"{self.idSensor} : {self.name} (Unidade : {self.unit})"

    def toDict(self):
        return {
            "idSensor" : self.idSensor,
            "idLocation" : self.idLocation,
            "name" : self.name,
            "unit": self.unit
        }

    @staticmethod
    def fromDict(data : dict):
        return Sensor(data.get("idSensor", None), data.get("idLocation", None), data["name"], data["unit"])

class Reading(Base):
    __tablename__ = 'reading'

    def __init__(self, idReading: int, idSensor: int, value: float):
        self.idReading = idReading
        self.idSensor = idSensor
        self.value = value
    
    idReading = sa.Column(sa.Integer(), primary_key = True)
    idSensor = sa.Column(sa.Integer, sa.ForeignKey(Sensor.idSensor))
    value = sa.Column(sa.Float(45))

    def __repr__(self):
        return f"{self.idReading} (Sensor {self.idSensor}) : {self.value}"

    def toDict(self):
        return {
            "idReading" : self.idReading,
            "idSensor" : self.idSensor,
            "value": self.value
        }

    @staticmethod
    def fromDict(data : dict):
        return Reading(data.get("idReading", None), data.get("idSensor", None), data["value"])

class Alert(Base):
    __tablename__ = 'alert'

    def __init__(self, idAlert: int, idSensor: int, description: str, cleared: bool):
        self.idAlert = idAlert
        self.idSensor = idSensor
        self.description = description
        self.cleared = cleared

    idAlert = sa.Column(sa.Integer(), primary_key = True)
    idSensor = sa.Column(sa.Integer, sa.ForeignKey(Sensor.idSensor))
    description = sa.Column(sa.String(45))
    cleared = sa.Column(sa.Boolean)


    def toDict(self):
        return {
            "idAlert" : self.idAlert,
            "idSensor" : self.idSensor,
            "description" : self.description,
            "cleared": self.cleared
        }

    @staticmethod
    def fromDict(data : dict):
        return Alert(data.get("idAlert", None), data.get("idSensor", None), data["description"], data["cleared"])


if __name__ == "__main__":
    url = 'sqlite:///sensors.db'
    engine = sa.create_engine(url)
    Session = sa_orm.sessionmaker(bind = engine)
    with Session() as s:
        Base.metadata.create_all(engine)
        if s.get(Sensor, 0):
            for _ in range(20):
                reading = Reading(None, 0, random.random())
                s.add(reading)
        s.commit()
        pass