# -------------------------------------------------------------------------------------------------
#  CLASSE PESSOA
# -------------------------------------------------------------------------------------------------
class Person:
    def __init__(self, forename, surname, address, cc, phone_number):
        self.__forename = forename
        self.__surname = surname
        self.__address = address
        self.__cc = cc
        self.__phone_number = phone_number

    @property
    def forename(self):
        return self.__forename

    @forename.setter
    def forename(self, value):
        self.__forename = value

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        self.__surname = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    @property
    def cc(self):
        return self.__cc

    @cc.setter
    def cc(self, value):
        self.__cc = value

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        self.__phone_number = value

# Exemplo de uso
person1 = Person("John", "Doe", "123 Main St", "123456789", "555-1234")


print("Forename:", person1.forename)
print("Surname:", person1.surname)
print("Address:", person1.address)
print("CC:", person1.cc)
print("Phone Number:", person1.phone_number)


person1.forename = "Jane"
person1.surname = "Smith"
person1.address = "456 Oak St"
person1.cc = "987654321"
person1.phone_number = "555-5678"


print("\nApós Modificação:")
print("Forename:", person1.forename)
print("Surname:", person1.surname)
print("Address:", person1.address)
print("CC:", person1.cc)
print("Phone Number:", person1.phone_number)


# ------------------------------------------
#  CLASSE CARRO
# ------------------------------------------

class Car:
    def __init__(self, brand, model, consumption, kms, owner):
        self._carBrand = brand
        self._carModel = model
        self._carConsumption = consumption
        self._carKms = kms
        self._carOwner = owner

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

# Exemplo de uso
carro = Car("Toyota", "Corolla", 15.5, 50000, None)

# Acessando campos usando a propriedade
print("Marca do carro:", carro.carBrand)
print("Modelo do carro:", carro.carModel)
print("Consumo do carro:", carro.carConsumption)
print("Quilômetros do carro:", carro.carKms)
print("Proprietário do carro:", carro.carOwner)

# Modificando campos usando a propriedade
carro.carBrand = "Honda"
carro.carModel = "Civic"
carro.carConsumption = 14.0
carro.carKms = 60000
carro.carOwner = "Alice"

# Exibindo os campos após a modificação
print("\nApós Modificação:")
print("Marca do carro:", carro.carBrand)
print("Modelo do carro:", carro.carModel)
print("Consumo do carro:", carro.carConsumption)
print("Quilômetros do carro:", carro.carKms)
print("Proprietário do carro:", carro.carOwner)

# ------------------------------------------
#  CLASSE ENGINE
# ------------------------------------------


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


class Car:
    def __init__(self, brand, model, consumption, kms, owner, engine):
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

# Exemplo de uso
engine = Engine("Gasolina", 150, 200, 2000, 4, "Elétrico", 150, "Toyota")
carro = Car("Toyota", "Corolla", 15.5, 50000, None, engine)

# Acessando campos usando a propriedade
print("Marca do carro:", carro.carBrand)
print("Modelo do carro:", carro.carModel)
print("Consumo do carro:", carro.carConsumption)
print("Quilômetros do carro:", carro.carKms)
print("Proprietário do carro:", carro.carOwner)
print("\nDetalhes do motor:")
print("Combustível:", carro.engine.fuel)
print("Potência:", carro.engine.horsepower)
print("Torque:", carro.engine.torque)
print("Deslocamento:", carro.engine.displacement)
print("Número de cilindros:", carro.engine.numCylinders)
print("Sistema de partida:", carro.engine.startingSystem)
print("Peso seco:", carro.engine.dryWeight)
print("Fabricante do motor:", carro.engine.manufacturer)