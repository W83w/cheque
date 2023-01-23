from main import Person
spam = Person("Spam SP")
print(spam.name, spam.pay) 
print(spam.name.split()[-1])    # получил фамилию

pay = 10000
pay *= 1.10 # Повышение заработной п
print(f'{spam.name} получает зарплату {pay}')