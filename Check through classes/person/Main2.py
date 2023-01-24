from main import Person
# Добавление метода перезагрузки операции __repr__ для вывода объектов
class Person1:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    def __repr__(self):         # Добавляет метод
        return '[Person: %s , %s]' % (self.name, self.pay) # Строка для вывода
class Manager(Person1):
    def __init__(self, name, pay):
        Person1.__init__(self, name, 'mgr', pay)
    def giveRaise(self, percent, bonus = .10):
        Person1.giveRaise(self, percent + bonus)
class Department: # Добавление кода самотестирования
    def __init__(self, *args):
        self.members = list(args)
    def addMember(self, person):
        self.members.append(person)
    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(person)
    def showAll(self):
        for person in self.members:
            print(person)


if __name__ == "__main__":
    bob = Person(name='Bob Smith')
    sue = Person("Sue jones", job='dev', pay=10000)
    print(bob.name)
    print(sue.name, sue.pay, sue.job)
    tom = Manager('Tom Jones', 50000) # Создал экземпляр
    tom.giveRaise(.10) # Выполняется специальная версия
    print(f"tom зарплата {tom.pay}")
    print(f'полное фио {tom.name}, отдельно фамилия {tom.lastName()}, работа и зарплата {tom.job}, {tom.pay}') # выполняется унаследованный метод
    print(tom) # Выполняется условие __repr__

    development = Department(bob, sue)
    development.addMember(tom)
    development.giveRaises
    development.showAll()