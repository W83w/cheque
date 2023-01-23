class Person: # начало класса
    def __init__(self, name, job=None, pay=0, lastName = None, giveRaise = 0): # добавляю метод конструктора и он принимает 3 аргумента
        # и выставил им стандартное значение нет работы и 0 заработная плата и эти 2 аргумента теперь не обязательны
        self.name = name # заполнитель поля при создании
        self.job = job # self новый объект экземпляра
        self.pay = pay
        self.lastName = lastName
        self.giveRaise = giveRaise
if __name__ == '__main__': # только тогда когда запускается для тестирования
# Добавление кода самотестирования
    bob = Person('Bob Smith') # Тестирование класса
    sue = Person("Sue Jones", job='dev', pay=100000) # Автоматически выполнит __init__

    print(bob.name, bob.pay) # извлечение присоединенных атрибутов
    print(sue.name, sue.pay) # Атрибуты sue  и bob отличаются
    print(bob.name.split()[-1]) # извлечение фамилии
    sue.pay *= 1.10  # Предоставление этому объекту повышение зп
    print(f'{sue.name} зп повышенна до {sue.pay}')

