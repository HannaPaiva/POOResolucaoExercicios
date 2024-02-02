
from car import Car
from person import Person
from engine import Engine
from color import Color


def list_persons(persons):
    print("\nLista de Pessoas:")
    for i, person in enumerate(persons, 1):
        print(f"{i}. {person.forename} {person.surname}")

def new_person(persons):
    forename = input("Nome: ")
    surname = input("Sobrenome: ")
    address = input("Endereço: ")
    cc = input("CC: ")
    phone_number = input("Número de telefone: ")

    person = Person(forename, surname, address, cc, phone_number)
    persons.append(person)
    print("Nova pessoa adicionada com sucesso!")


def delete_person(persons):
    list_persons(persons)
    index = int(input("Digite o número da pessoa que deseja apagar: ")) - 1
    if 0 <= index < len(persons):
        del persons[index]
        print("Pessoa removida com sucesso!")
    else:
        print("Número de pessoa inválido.")


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



def save_persons_to_file(persons, filename="person_list.txt"):
    with open(filename, "w") as file:
        for person in persons:
            file.write(f"{person.forename},{person.surname},{person.address},{person.cc},{person.phone_number}\n")
    print(f"Lista de pessoas salva no arquivo: {filename}")


def list_cars(cars):
    print("\nLista de Carros:")
    for i, car in enumerate(cars, 1):
        print(f"{i}. {car.carBrand} {car.carModel} (Proprietário: {car.carOwner})")


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


def delete_car(cars):
    list_cars(cars)
    index = int(input("Digite o número do carro que deseja apagar: ")) - 1
    if 0 <= index < len(cars):
        del cars[index]
        print("Carro removido com sucesso!")
    else:
        print("Número de carro inválido.")

def edit_car(cars, persons):
    list_cars(cars)
    car_color = Color("Red", 255, 0, 0)

    index = int(input("Digite o número do carro que deseja editar: ")) - 1
    if 0 <= index < len(cars):
        car = cars[index]
        car.carBrand = input("Nova marca do carro: ")
        car.carModel = input("Novo modelo do carro: ")
        car.carConsumption = float(input("Novo consumo do carro (km/l): "))
        car.carKms = float(input("Novos quilômetros do carro: "))
        car.color = (car_color)
        owner_index = int(input("Digite o número do novo proprietário do carro: ")) - 1
        if 0 <= owner_index < len(persons):
            car.carOwner = persons[owner_index].forename + " " + persons[owner_index].surname
            print("Carro editado com sucesso!")
        else:
            print("Número de proprietário inválido.")
    else:
        print("Número de carro inválido.")


def save_cars_to_file(cars, filename="car_list.txt"):
    with open(filename, "w") as file:
        for car in cars:
            file.write(f"{car.carBrand},{car.carModel},{car.carConsumption},{car.carKms},{car.carOwner}, {car.color}\n")
    print(f"Lista de carros salva no arquivo: {filename}")


def main():
    persons = []  # Lista de pessoas
    cars = []  # Lista de carros

    while True:
        print("\nMenu:")
        print("1 - Lista de pessoas")
        print("2 - Nova pessoa")
        print("3 - Apagar pessoa")
        print("4 - Editar pessoa")
        print("5 - Lista de carros")
        print("6 - Novo carro")
        print("7 - Apagar carro")
        print("8 - Editar carro")
        print("9 - Gravar em arquivo")
        print("0 - Sair")

        option = input("Escolha uma opção: ")

        if option == "1":
            list_persons(persons)
        elif option == "2":
            new_person(persons)
        elif option == "3":
            delete_person(persons)
        elif option == "4":
            edit_person(persons)
        elif option == "5":
            list_cars(cars)
        elif option == "6":
            new_car(cars, persons)
        elif option == "7":
            delete_car(cars)
        elif option == "8":
            edit_car(cars, persons)
        elif option == "9":
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
