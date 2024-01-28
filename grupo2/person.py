# person.py

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
