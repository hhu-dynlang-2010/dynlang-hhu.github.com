import py
import os

# ____________________________________________________________
#
# AUFGABE 1
#

def test_count_lines_and_words():
    try:
        f = file("test.txt", "w")
        f.write("a bc def ghi\n" * 16)
        f.close()
        lines, words = count_lines_and_words('test.txt')
        assert lines == 16
        assert words == 4 * 16
    finally:
        os.unlink("test.txt")

# ____________________________________________________________
#
# AUFGABE 2
#
import math

EPSILON = 0.0001

def test_find_zero():
    res = find_zero(math.cos, 0, 2)
    assert abs(res - math.pi/2.0) <= EPSILON

    def f(x):
        return (x-1) * x

    res = find_zero(f, 0.5, 100)
    assert abs(res - 1.0) <= EPSILON

    res = find_zero(f, -100, 0.5)
    assert abs(res - 0.0) <= EPSILON

def test_initial_condition():
    py.test.raises(ValueError, find_zero, math.cos, 0, 0.5)

def test_reversed_a_and_b():
    res = find_zero(math.cos, 2, 0)
    assert abs(res - math.pi/2.0) <= EPSILON


def test_sqrt():
    for num in [0, 0.2, 0.5, 1, 10, 41, 100]:
        assert abs(approximate_sqrt(num) - math.sqrt(num)) <= EPSILON


def test_make_function():
    # basic case
    f = make_function("x * 6")
    assert f(7) == 42

    # extended version: functions from the math module can be used too
    f = make_function("sin(x) - sqrt(x)")
    assert f(1.2) == math.sin(1.2) - math.sqrt(1.2)


def test_find_zero_from_string():
    # this should be just find_zero combined with make_function
    res = find_zero_from_string("cos(x)", 0, 2)
    assert abs(res - math.pi/2.0) <= EPSILON


# ____________________________________________________________
#
# AUFGABE 3
#

class A(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def f(self, z):
        return self.x + self.y + z

class B(A):
    def g(self):
        return self.x * 17

def test_send():
    a = A(12, 13)
    assert a.f(1) == 26
    assert send(a, "f", 1) == 26

    b = B(14, 15)
    assert b.f(-1) == 28
    assert send(b, "f", -1) == 28
    assert b.g() == 14 * 17
    assert send(b, "g") == 14 * 17

def test_send_not_found():
    a = A(12, 13)
    py.test.raises(AttributeError, "a.notthere(1)")
    py.test.raises(AttributeError, "send(a, 'notthere', 1)")

class C(A):
    def message_not_understood(self, message, *args):
        return ('we have seen', message, args)

def test_send_message_not_understood():
    c = C(16, 17)
    assert send(c, 'notthere', 1) == ('we have seen', 'notthere', (1,))


# ____________________________________________________________
#
# AUFGABE 4
#

def test_forward_transformation():
    # see http://de.wikipedia.org/wiki/Burrows-Wheeler-Transformation
    assert burrows_wheeler_forward("TEXTUEL") == ("UTELXTE", 3)

    input = ("TRENTATRE.TRENTINI.ANDARONO.A.TRENTO"
             ".TUTTI.E.TRENTATRE.TROTTERELLANDO")
    expected_output = ("OIIEEAEO..LDTTNN.RRRRRRRTNTTLE"
                       "AAIOEEEENTRDRTTETTTTATNNTTNNAAO....OU.T")
    assert burrows_wheeler_forward(input) == (expected_output, 60)


def test_backward_transformation():
    xxx   # write the test!


def test_composition():
    f = open('blatt1.py', 'r')
    text = f.read()
    f.close()
    (transformed, index) = burrows_wheeler_forward(text)
    output = burrows_wheeler_backward(transformed, index)
    assert output == text
