from main import Person

def lastName (self):  # методы реализации поведения
    return self.name.split()[-1] # self подразумеваемый объект
def giveRaise(self, percent):
    self.pay = int(self.pay * (1 + percent)) # поработал с классом но изменил только тут чтобы сдать код более
    # приспособленным к изменениям
if __name__ == '__main__':  # только тогда когда запускается для тестирования
        # Добавление кода самотестирования
    bob = Person('Bob Smith')  # Тестирование класса
    sue = Person("Sue Jones", job='dev', pay=100000)  # Автоматически выполнит __init__

    print(bob.name, bob.pay)  # извлечение присоединенных атрибутов
    print(sue.name, sue.pay)  # Атрибуты sue  и bob отличаются
    print(bob.name.split()[-1])  # извлечение фамилии
    sue.pay *= 1.10  # Предоставление этому объекту повышение зп
    print(f'{sue.name} зп повышенна до {sue.pay}')
    print(bob.lastName, sue.lastName) # использую новые методы вместо жесткого кодирования
    print(sue.pay)