import sqlalchemy as sa
import sqlalchemy.orm as db
import models

Base = db.declarative_base()

def get_location(s) -> models.Location:
    while True:
        localizacao = input("Introduza a localização: ")
        locations = s.query(models.Location).filter(models.Location.name.like(localizacao)).all()

        if len(locations) == 1:
            return locations[0]

        elif len(locations) == 0:
            criar_nova = input("Esta localização não é reconhecida. Deseja criar uma nova localização? (S/N) ")
            if criar_nova.upper() == "S":
                descricao = input("Introduza a descrição da nova localização: ")
                location = models.Location(None, localizacao, descricao)
                s.add(location)
                return location
        else:
            print("Foram encontradas várias localizações com esse nome. Selecione uma:")
            for location in locations:
                print(location)
            loc_id = int(input())
            location = [x for x in locations if x.idLocation == loc_id]
            # Itera a lista locations adicionando cada elemento x à nova lista se o valor do atributo do x de idLocation for igual ao valor da variável "loc_id"
            # O que faz com que este consiga ir buscar a informação do locations com o id especificado no input
            if len(location) == 0:
                print("Localização inválida.")
            else:
                return location[0]

def get_unit(s) -> models.Unit:
    while True:
        unidade = input("Introduza a unidade de medida para o novo sensor: ")
        units = s.query(models.Unit).filter(models.Unit.unit.like(unidade)).all()
        #Este comando vai buscar todas as insereções de dados da variável unidade na tabela Unit

        if len(units) == 1:
            return units[0]

        elif len(units) == 0:
            criar_nova = input("Esta unidade não é reconhecida. Deseja criar uma nova unidade? (S/N) ")
            if criar_nova.upper() == "S":
                descricao = input("Introduza a descrição da nova unidade: ")
                unit = models.Unit(unidade, descricao)
                s.add(unit)
                return unit
        else:
            print("Foram encontradas várias unidades com esse nome. Selecione uma:")
            for unit in units:
                print(unit)
            unit_id = input()
            unit = [x for x in units if unit.unit == unit_id]
            if len(unit) == 0:
                print("Unidade inválida.")
            else:
                return unit[0]

def introduzir_novo_sensor(s):
    # Pedir o nome do sensor
    nome_sensor = input("Introduza o nome do novo sensor: ")

    # Verificar se a localização existe
    
    location = get_location(s)

    # Verificar se a unidade existe
    unidade = get_unit(s)

    # Adicionar novo sensor à lista de sensores
    
    sensor = models.Sensor(None, location.idLocation, nome_sensor, unidade.unit)
    s.add(sensor)
    s.commit()

    print("Novo sensor adicionado com sucesso!")

def atualizar_leituras(s):
    readings = s.query(models.Reading).all()

    if len(readings) == 0:
        print("Ainda não existem leituras")
        return
    
    sensors = s.query(models.Sensor).all()
    print("Sensores:")
    for sensor in sensors:
        print(sensor)

    print("-------------------------------")

    valid_keys = [x.idReading for x in readings]

    for reading in readings:
        print(reading)
    
    selected_reading = int(input("Selecione a leitura a editar: "))
    if selected_reading in valid_keys:
        value = float(input("Selecione o novo valor para a leitura:"))
        reading = [x for x in readings if x.idReading == selected_reading][0]
        reading.value = value
        s.add(reading)
        s.commit()
    else:
        print("Leitura inválida")


def alterar_localizacao_sensor(s):
    sensors = s.query(models.Sensor).all()

    for sensor in sensors:
        print(sensor)

    valid_keys = [x.idSensor for x in sensors]

    selected_sensor = int(input("Selecione o sensor para alterar: "))
    if selected_sensor in valid_keys:
        selected_sensor = [x for x in sensors if x.idSensor == selected_sensor][0]
        location = get_location(s)
        selected_sensor.idLocation = location.idLocation
        s.merge(selected_sensor)
        s.commit()
        print("Localização atualizada com sucesso")
    else:
        print("Sensor inválido")

def remover_leituras(s):
    readings = s.query(models.Reading).all()

    if len(readings) == 0:
        print("Ainda não existem leituras")
        return
    
    sensors = s.query(models.Sensor).all()
    print("Sensores:")
    for sensor in sensors:
        print(sensor)

    print("-------------------------------")

    valid_keys = [x.idReading for x in readings]

    for reading in readings:
        print(reading)
    
    selected_reading = int(input("Selecione a leitura a remover: "))
    if selected_reading in valid_keys:
        reading = [x for x in readings if x.idReading == selected_reading][0]
        s.delete(reading)
        s.commit()
    else:
        print("Leitura não encontrada")

def ver_informacao_sensor(s):
    sensors = s.query(models.Sensor).all()

    while True:
        for sensor in sensors:
            print(sensor)

        valid_keys = [x.idSensor for x in sensors]

        selected_sensor = int(input("Selecione o sensor para visualizar: "))
        if selected_sensor in valid_keys:
            selected_sensor = [x for x in sensors if x.idSensor == selected_sensor][0]
            print(selected_sensor)
            location = s.get(models.Location, selected_sensor.idLocation)
            print("Localização: ")
            print(location)

            last_10_readings = s.query(models.Reading).filter(models.Reading.idSensor == selected_sensor.idSensor).order_by(models.Reading.idReading.desc()).limit(10)
            print("Últimas 10 leituras")
            for reading in last_10_readings:
                print(reading)
            break

def sair(s):
    s.close()
    print("A sair e gravar...")
    exit()

if __name__ == "__main__":
    options = {
        "1": introduzir_novo_sensor,
        "2": atualizar_leituras,
        "3": alterar_localizacao_sensor,
        "4": remover_leituras,
        "5": ver_informacao_sensor,
        "6": sair
    }
    url = 'sqlite:///sensors.db'
    engine = sa.create_engine(url)
    Base.metadata.create_all(engine)
    Session = db.sessionmaker(bind = engine)
    s = Session()
    while True:
        print("\n\nMenu:")
        print("1. Introduzir novo sensor")
        print("2. Atualizar leituras")
        print("3. Alterar localização do sensor")
        print("4. Remover leituras")
        print("5. Ver informação de sensor")
        print("6. Sair")
        choice = input("Introduza a sua escolha (1-6): ")
        if choice not in options.keys():
            print("Escolha inválida. Escolha uma opção válida (1-6).")
            continue
        options[choice](s)
