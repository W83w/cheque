from main import Person
# Хороший способ в python предусматривает вызов исходной версии напрямую с дополнительными аргументами
class Manager(Person):
    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)# Хороший способ: расширение исходной версии

bob = Manager('Tom Jones', 'mgr', '50000')