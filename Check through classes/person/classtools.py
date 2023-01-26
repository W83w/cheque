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