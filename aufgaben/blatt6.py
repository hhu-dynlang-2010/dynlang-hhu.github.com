import py

class Klass(object):
    def __init__(self, name, *parents):
        self.name = name
        self.parents = parents

    def getparents(self):
        return parents

    def get_mro(self):
        XXX # implement me

def test_simple():
    k1 = Klass("a")
    assert k1.get_mro() == [k1]
    k2 = Klass("b", k1)
    assert k2.get_mro() == [k2, k1]
    k3 = Klass("c", k2, k1)
    assert k3.get_mro() == [k3, k2, k1]


