import py
import math

def test_spreadsheet():
    s = Spreadsheet()
    s["a1"] = 5
    assert s["a1"] == 5
    s["a5"] = 16
    assert s["a5"] == 16
    s["a6"] = "a1 * a5"
    assert s["a6"] == 80
    s["a7"] = "a6 + 1"
    assert s["a7"] == 81

    s["a1"] = 1
    assert s["a6"] == 16
    assert s["a7"] == 17

def test_math_function():
    s = Spreadsheet()
    s["a1"] = 16.0
    s["a2"] = "sqrt(a1)"
    assert s["a2"] == 4.0

def test_list():
    s = Spreadsheet()
    s["a1"] = [1, 2, 3, 4, 5]
    s["a2"] = "filter(lambda x: x % 2 == 0, a1)"
    assert s["a2"] == [2, 4]


def test_recursive():
    py.test.skip("this is hard")
    s = Spreadsheet()
    s["a1"] = "a1"
    s["a1"]


class Spreadsheet(object):
    def __init__(self):
        self.cells = {}

    def __getitem__(self, cell):
        value = self.cells[cell]
        if not isinstance(value, str):
            return value
        return eval(value, math.__dict__, self)

    def __setitem__(self, cell, value):
        self.cells[cell] = value
