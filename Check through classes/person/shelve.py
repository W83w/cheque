#!/usr/bin/env python
# coding: utf-8

# In[1]:



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
    bob = Person1(name='Bob Smith')
    sue = Person1("Sue jones", job='dev', pay=10000)
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


# In[2]:


bob = Person1('Bob Smith')
sue = Person1('Sue jones', job = 'dev', pay=1000000)
tom = Manager('Tom Jones', 50000)


# In[3]:


class AttrDisplay:
    '''
    Предоставляет наследуемый метод перезагрузки отображения, который поназывает экземпляры с мх именами классов
    и пары имя = значение для каждого атрибута, сохраненного в самом экземпляре(но не атрибутов, унаследованных от
    классов).
    Может соединятся с любым классом и будет работать на любом экземпляре
    '''
    def gatherAttrrs(self):
        atters = []
        for key in sorted(self.__dict__):
            atters.append('%s=%s' % (key, getattr(self, key)))
        return ",".join(atters)
    def __repr__(self):
        return str((self.__class__.__name__, self.gatherAttrrs()))

class TopTest(AttrDisplay):
    count = 0
    def __init__(self):
        self.attr1 = TopTest.count
        self.attr2 = TopTest.count+1
        TopTest.count+=2

class SubTest(TopTest):
    pass


X, Y = TopTest(), SubTest()
print(X, Y)


# In[4]:


import shelve 
db = shelve.open('persondb')
for obj in (bob, sue, tom):
    db[obj.name] = obj
db.close()


# In[5]:


import glob
glob.glob('person*')
print(open('persondb.dir').read())


# In[6]:


db = shelve.open('persondb')
len(db.keys())
bob = db['Bob Smith']
print(bob)
sue = db['Sue jones']
print(sue)


# In[7]:


bob.lastName()
for key in db:
    print(key, '=>', db[key])
for key in sorted(db):
    print(key, '=>', db[key])


# In[15]:


# повышение зп
db = shelve.open("persondb")

for kay in sorted(db):
    print(key, '\t=>', db[key])
sue = db['Sue jones']
sue.giveRaise(.10)
db['Sue jones'] = sue
db.close()

db=shelve.open('persondb')
rec = db['Sue jones']
print(rec)
rec.lastName()
rec.pay

