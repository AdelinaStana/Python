'''
todo: build interpreter based on commands
nume, prenume, varsta
>print nume varsta prenume
>print nume ORDERBY varsta
>print etc
>add Person name = n surname = s age = a
'''


class Person:
    def __init__(self, name="", surname="", age=""):
        self.name = name
        self.surname = surname
        self.age = age

    def get_attribute_val(self, attrib):
        for attribute in self.__dict__.keys():
            if attribute[:2] != '__':
                value = getattr(self, attribute)
                if attribute == attrib:
                    return value
        return attrib

    def set_attribute_val(self, attrib, val):
        for attribute in self.__dict__.keys():
            if attribute[:2] != '__':
                if attribute == attrib:
                    setattr(self, attribute, val)


class DataBase:
    def __init__(self):
        self.persons = []

    def add_person(self, name, surname, age):
        p = Person(name, surname, age)
        self.persons.append(p)

    def order_by(self, attribute):
        self.persons.sort(key=lambda x: x.get_attribute_val(attribute), reverse=False)


class Interpreter:
    def __init__(self, db):
        self.db = db

    def print(self, command_elements):
        for person in self.db.persons:
            output_line = " "
            for attrib in command_elements:
                output_line += str(person.get_attribute_val(attrib)) + " "
            print(output_line)

    def order_print(self, command_elements, orders):
        for order in orders:
            self.db.order_by(order)

        self.print(command_elements)

    def add_person(self, command_elements):
        p = Person()
        for index in range(0, len(command_elements)):
            if command_elements[index] == '=':
                p.set_attribute_val(command_elements[index - 1], command_elements[index + 1])

        self.db.persons.append(p)

    def interpret(self, command):
        if command.startswith('print'):
            command = command.replace('print', ' ')
            if 'ORDER' in command:
                command_first = command.split('ORDER')[0]
                command_order = command.split('ORDER')[1]
                self.order_print(command_first.split(' '), command_order.split(' '))
            else:
                self.print(command.split(' '))

        if command.startswith('add Person'):
            command = command.replace('add Person', ' ')
            self.add_person(command.split(' '))


if __name__ == '__main__':
    command = ""
    db = DataBase()

    db.add_person('Ionescu', 'Ion', 20)
    db.add_person('Vasilescu', 'Ion', 26)
    db.add_person('Alexandrescu', 'Alex', 46)

    interpreter = Interpreter(db)

    while command != 'exit':
        command = input("Enter command: ")
        interpreter.interpret(command)

    print("Bye bye!")