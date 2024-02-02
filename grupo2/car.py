class Car:
    def __init__(self, brand, model, consumption, kms, owner, engine=None):
        self._carBrand = brand
        self._carModel = model
        self._carConsumption = consumption
        self._carKms = kms
        self._carOwner = owner
        self._engine = engine 

    @property
    def carBrand(self):
        return self._carBrand

    @carBrand.setter
    def carBrand(self, value):
        self._carBrand = value

    @property
    def carModel(self):
        return self._carModel

    @carModel.setter
    def carModel(self, value):
        self._carModel = value

    @property
    def carConsumption(self):
        return self._carConsumption

    @carConsumption.setter
    def carConsumption(self, value):
        self._carConsumption = value

    @property
    def carKms(self):
        return self._carKms

    @carKms.setter
    def carKms(self, value):
        self._carKms = value

    @property
    def carOwner(self):
        return self._carOwner

    @carOwner.setter
    def carOwner(self, value):
        self._carOwner = value

    @property
    def engine(self):
        return self._engine

    @engine.setter
    def engine(self, value):
        self._engine = value
