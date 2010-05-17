import py

def test_vector():
    a = Vector([1, 2, 3])
    b = Vector([2, 4, 6])
    c = a + b
    assert c == Vector([3, 6, 9])
    assert not c != Vector([3, 6, 9])

def test_different_length():
    a = Vector([1, 2, 3])
    b = Vector([2, 4, 6, 7])
    py.test.raises(ValueError, "a + b")
    py.test.raises(ValueError, "b + a")

def test_mul():
    a = Vector([1, 2, 3, 4])
    b = a * 5
    assert b == Vector([5, 10, 15, 20])
    b = 5 * a
    assert b == Vector([5, 10, 15, 20])


class Vector(object):
    def __init__(self, l):
        self.components = l

    def _check_lengths(self, other):
        if len(self.components) != len(other.components):
            raise ValueError

    def __add__(self, other):
        self._check_lengths(other)
        result = []
        for i in range(len(self.components)):
            result.append(self.components[i] + other.components[i])
        return Vector(result)

    def __mul__(self, other):
        result = []
        for elt in self.components:
            result.append(elt * other)
        return Vector(result)

    def __rmul__(self, other):
        return self * other


    def __eq__(self, other):
        return self.components == other.components

    def __ne__(self, other):
        return not self == other
