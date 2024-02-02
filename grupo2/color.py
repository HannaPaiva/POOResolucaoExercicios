class Color:
    def __init__(self, color_name, r, g, b):
        self._color_name = color_name
        self._r = r
        self._g = g
        self._b = b

    @property
    def color_name(self):
        return self._color_name

    @color_name.setter
    def color_name(self, new_color_name):
        self._color_name = new_color_name

    @property
    def rgb(self):
        return self._r, self._g, self._b

    @rgb.setter
    def rgb(self, new_rgb):
        self._r, self._g, self._b = new_rgb


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
    def num_cylinders(self):
        return self._num_cylinders

    @num_cylinders.setter
    def num_cylinders(self, value):
        self._num_cylinders = value

    @property
    def starting_system(self):
        return self._starting_system

    @starting_system.setter
    def starting_system(self, value):
        self._starting_system = value

    @property
    def dry_weight(self):
        return self._dry_weight

    @dry_weight.setter
    def dry_weight(self, value):
        self._dry_weight = value

    @property
    def manufacturer(self):
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        self._manufacturer = value


class Car:
    def __init__(self, brand, model, consumption, kms, owner, color, engine=None):
        self._brand = brand
        self._model = model
        self._consumption = consumption
        self._kms = kms
        self._owner = owner
        self._engine = engine
        self._color = color

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @property
    def consumption(self):
        return self._consumption

    @consumption.setter
    def consumption(self, value):
        self._consumption = value

    @property
    def kms(self):
        return self._kms

    @kms.setter
    def kms(self, value):
        self._kms = value

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = value

    @property
    def engine(self):
        return self._engine

    @engine.setter
    def engine(self, value):
        self._engine = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if not isinstance(value, Color):
            raise ValueError("Precisa ser uma instância da classe")
        self._color = value


if __name__ == "__main__":
 
    car_color = Color("Red", 255, 0, 0)

    car_engine = Engine("Gasolina", 200, 180, 3000, 6, "Eletrico", 150, "blasbaksaksas")

    carro = Car("Toyota", "Camry", 12, 50000, "John Doe", car_color, car_engine)


    print(f"Marca: {carro.brand}")
    print(f"Modelo: {carro.model}")
    print(f"Consumo: {carro.consumption} km/l")
    print(f"Kms: {carro.kms} km")
    print(f"Dono: {carro.owner}")
    print(f"Cor: {carro.color.color_name}")
    print(f"Horsepower da engine: {carro.engine.horsepower} ")

   
