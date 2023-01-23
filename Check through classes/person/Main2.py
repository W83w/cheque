from main import Person
# Добавление метода перезагрузки операции __repr__ для вывода объектов
class Person1(Person):
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
class Manager(Person):
    def giveRaise(self, percent, bonus=.10):
        super().percent = percent
        Person.giveRaise(self, percent + bonus)  # Хороший способ: расширение исходной версии

if __name__ == "__main__":
    bob = Person(name='Bob Smith')
    sue = Person("Sue jones", job='dev', pay=10000)
    print(bob.name)
    print(sue.name, sue.pay, sue.job)
    tom = Manager('Tom Jones', 'mgr', '50000') # Создал экземпляр
    tom.giveRaise # Выполняется специальная версия
    print(f"tom зарплата {tom.pay}")
    print(tom.name) # выполняется унаследованный метод
    print(tom) # Выполняется условие __repr__





