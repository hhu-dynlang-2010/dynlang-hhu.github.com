
def test_logging_proxy_simple():
    class A(object):
        def __init__(self, a):
            self.a = a

        def f(self, x):
            result = self.a
            self.a = x
            return result

    a = A(1)
    p = LoggingProxy(a)
    assert p.a == 1
    attr = p.f(10)
    assert attr == 1
    assert p.a == 10
    assert get_proxy_log(p) == ["a", "f", "a"]

def test_logging_proxy_special():
    p = LoggingProxy(41.0)
    assert p + 2 == 43.0
    assert p - 2 == 39.0
    assert p == 41.0
    assert p
    assert p * 2 == 82.0
    assert p // 2 == 20.0
    assert p > 1.0
    assert get_proxy_log(p) == ["__add__", "__sub__", "__eq__", "__nonzero__",
                                "__mul__", "__floordiv__", "__gt__"]


# ____________________________________________________________


SQUARE = set([(0,0), (0,1),
              (1,0), (1,1)])
HLINE = set([(-1,0), (0,0), (1,0)])
VLINE = set([(0,-1), (0,0), (0,1)])

GLIDER = set([       (0,-1),
                             (1,0),
              (-1,1), (0,1), (1,1)])

SHIFTED_GLIDER = set([(x+1,y+1) for (x,y) in GLIDER])


def test_life_step():
    assert lifestep(set()) == set()
    assert lifestep(set([(0,0)])) == set()

    assert lifestep(SQUARE) == SQUARE
    assert lifestep(set([(0,0), (0,1),
                         (1,0)       ])) == SQUARE

    assert lifestep(HLINE) == VLINE
    assert lifestep(VLINE) == HLINE

    assert lifestep(lifestep(lifestep(lifestep(GLIDER)))) == SHIFTED_GLIDER


def test_life_string():
    assert lifestring(set()) == ""
    assert lifestring(set([(0,0)])) == "X"
    assert lifestring(set([(10,-5),(12,-5)])) == "X X"

    assert lifestring(SQUARE) == "XX\nXX"    # '\n' is an end-of-line character
    assert lifestring(set([(0,0), (0,1),
                         (1,0)       ])) == "XX\nX "

    assert lifestring(HLINE) == "XXX"
    assert lifestring(VLINE) == "X\nX\nX"

    assert lifestring(GLIDER) == (" X \n" +
                                  "  X\n" +
                                  "XXX")
    assert lifestring(SHIFTED_GLIDER) == lifestring(GLIDER)


def test_life_big():
    state = set([        (0,-1), (1,-1),
                 (-1,0), (0,0),
                         (0,1)          ])
    for i in range(1103):
        # for fun, print the first 100 iterations
        if i < 200:
            print '-'*80
            print lifestring(state)
            import time; time.sleep(0.1)
        state = lifestep(state)
    resulting_string = lifestring(state)    # big! about 500x500...
    assert hash(resulting_string) == 1756931965
