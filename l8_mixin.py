
class Base(object):
    pass

class NotEqMixin(object):
    def __ne__(self, other):
        return not self == other


class A(Base, NotEqMixin):
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value


def test_eq():
    a1 = A(1)
    a2 = A(1)
    assert a1 == a2
    assert not a1 != a2

class CmpMixin(NotEqMixin):
    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not (self <= other)

    def __ge__(self, other):
        return not (self < other)

class B(A, CmpMixin):
    def __lt__(self, other):
        return self.value < other.value


def test_lt():
    a1 = B(1)
    a2 = B(2)
    assert a1 < a2
    assert a1 <= a2

