# Importe as classes que você já definiu
from car import Car
from person import Person
from engine import Engine


# Função para listar pessoas
def list_persons(persons):
    print("\nLista de Pessoas:")
    for i, person in enumerate(persons, 1):
        print(f"{i}. {person.forename} {person.surname}")


# Função para inserir uma nova pessoa
def new_person(persons):
    forename = input("Nome: ")
    surname = input("Sobrenome: ")
    address = input("Endereço: ")
    cc = input("CC: ")
    phone_number = input("Número de telefone: ")

    person = Person(forename, surname, address, cc, phone_number)
    persons.append(person)
    print("Nova pessoa adicionada com sucesso!")


# Função para remover uma pessoa
def delete_person(persons):
    list_persons(persons)
    index = int(input("Digite o número da pessoa que deseja apagar: ")) - 1
    if 0 <= index < len(persons):
        del persons[index]
        print("Pessoa removida com sucesso!")
    else:
        print("Número de pessoa inválido.")


# Função para editar uma pessoa
def edit_person(persons):
    list_persons(persons)
    index = int(input("Digite o número da pessoa que deseja editar: ")) - 1
    if 0 <= index < len(persons):
        person = persons[index]
        person.forename = input("Novo nome: ")
        person.surname = input("Novo sobrenome: ")
        person.address = input("Novo endereço: ")
        person.cc = input("Novo CC: ")
        person.phone_number = input("Novo número de telefone: ")
        print("Pessoa editada com sucesso!")
    else:
        print("Número de pessoa inválido.")


# Função para salvar a lista de pessoas em um arquivo
def save_persons_to_file(persons, filename="person_list.txt"):
    with open(filename, "w") as file:
        for person in persons:
            file.write(f"{person.forename},{person.surname},{person.address},{person.cc},{person.phone_number}\n")
    print(f"Lista de pessoas salva no arquivo: {filename}")


# Função para listar carros
def list_cars(cars):
    print("\nLista de Carros:")
    for i, car in enumerate(cars, 1):
        print(f"{i}. {car.carBrand} {car.carModel} (Proprietário: {car.carOwner})")


# Função para inserir um novo carro
def new_car(cars, persons):
    list_persons(persons)
    owner_index = int(input("Digite o número do proprietário do carro: ")) - 1
    if 0 <= owner_index < len(persons):
        brand = input("Marca do carro: ")
        model = input("Modelo do carro: ")
        consumption = float(input("Consumo do carro (km/l): "))
        kms = float(input("Quilômetros do carro: "))
        owner = persons[owner_index].forename + " " + persons[owner_index].surname

        car = Car(brand, model, consumption, kms, owner)
        cars.append(car)
        print("Novo carro adicionado com sucesso!")
    else:
        print("Número de proprietário inválido.")


# Função para remover um carro
def delete_car(cars):
    list_cars(cars)
    index = int(input("Digite o número do carro que deseja apagar: ")) - 1
    if 0 <= index < len(cars):
        del cars[index]
        print("Carro removido com sucesso!")
    else:
        print("Número de carro inválido.")


# Função para editar um carro
def edit_car(cars, persons):
    list_cars(cars)
    index = int(input("Digite o número do carro que deseja editar: ")) - 1
    if 0 <= index < len(cars):
        car = cars[index]
        car.carBrand = input("Nova marca do carro: ")
        car.carModel = input("Novo modelo do carro: ")
        car.carConsumption = float(input("Novo consumo do carro (km/l): "))
        car.carKms = float(input("Novos quilômetros do carro: "))
        owner_index = int(input("Digite o número do novo proprietário do carro: ")) - 1
        if 0 <= owner_index < len(persons):
            car.carOwner = persons[owner_index].forename + " " + persons[owner_index].surname
            print("Carro editado com sucesso!")
        else:
            print("Número de proprietário inválido.")
    else:
        print("Número de carro inválido.")


# Função para salvar a lista de carros em um arquivo
def save_cars_to_file(cars, filename="car_list.txt"):
    with open(filename, "w") as file:
        for car in cars:
            file.write(f"{car.carBrand},{car.carModel},{car.carConsumption},{car.carKms},{car.carOwner}\n")
    print(f"Lista de carros salva no arquivo: {filename}")


# Função principal
def main():
    persons = []  # Lista de pessoas
    cars = []  # Lista de carros

    while True:
        print("\nMenu:")
        print("11 - Lista de pessoas")
        print("12 - Nova pessoa")
        print("13 - Apagar pessoa")
        print("14 - Editar pessoa")
        print("21 - Lista de carros")
        print("22 - Novo carro")
        print("23 - Apagar carro")
        print("24 - Editar carro")
        print("99 - Gravar em arquivo")
        print("0 - Sair")

        option = input("Escolha uma opção: ")

        if option == "11":
            list_persons(persons)
        elif option == "12":
            new_person(persons)
        elif option == "13":
            delete_person(persons)
        elif option == "14":
            edit_person(persons)
        elif option == "21":
            list_cars(cars)
        elif option == "22":
            new_car(cars, persons)
        elif option == "23":
            delete_car(cars)
        elif option == "24":
            edit_car(cars, persons)
        elif option == "99":
            save_option = input("Deseja salvar a lista de pessoas em um arquivo? (s/n): ")
            if save_option.lower() == "s":
                save_persons_to_file(persons)
            save_option = input("Deseja salvar a lista de carros em um arquivo? (s/n): ")
            if save_option.lower() == "s":
                save_cars_to_file(cars)
            print("Listas salvas em arquivo.")
        elif option == "0":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
