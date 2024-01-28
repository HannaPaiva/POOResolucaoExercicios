# engine.py

class Engine:
    def __init__(self, fuel, horsepower, torque, displacement, num_cylinders, starting_system, dry_weight, manufacturer):
        self._fuel = fuel
        self._horsepower = horsepower
        self._torque = torque
        self._displacement = displacement
        self._num_cylinders = num_cylinders
        self._starting_system = starting_system
        self._dry_weight = dry_weight
        self._manufacturer = manufacturer

    @property
    def fuel(self):
        return self._fuel

    @fuel.setter
    def fuel(self, value):
        self._fuel = value

    @property
    def horsepower(self):
        return self._horsepower

    @horsepower.setter
    def horsepower(self, value):
        self._horsepower = value

    @property
    def torque(self):
        return self._torque

    @torque.setter
    def torque(self, value):
        self._torque = value

    @property
    def displacement(self):
        return self._displacement

    @displacement.setter
    def displacement(self, value):
        self._displacement = value

    @property
    def numCylinders(self):
        return self._num_cylinders

    @numCylinders.setter
    def numCylinders(self, value):
        self._num_cylinders = value

    @property
    def startingSystem(self):
        return self._starting_system

    @startingSystem.setter
    def startingSystem(self, value):
        self._starting_system = value

    @property
    def dryWeight(self):
        return self._dry_weight

    @dryWeight.setter
    def dryWeight(self, value):
        self._dry_weight = value

    @property
    def manufacturer(self):
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        self._manufacturer = value
