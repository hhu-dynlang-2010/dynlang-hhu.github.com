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
    import time
    state = set([        (0,-1), (1,-1),
                 (-1,0), (0,0),
                         (0,1)          ])
    for i in range(1103):
        # for fun, print the first 100 iterations
        if i < 200:
            print '-'*80
            print lifestring(state)
            time.sleep(0.1)
        state = lifestep(state)
    resulting_string = lifestring(state)    # big! about 500x500...
    assert hash(resulting_string) == 1756931965


SQUARE = set([(0,0), (0,1),
              (1,0), (1,1)])

def test_from_life_string():
    assert from_lifestring("") == set()
    assert from_lifestring("X") == set([(0,0)])
    assert from_lifestring("X X") == set([(0, 0), (0, 2)])

    assert from_lifestring("XX\nXX") == SQUARE
    assert from_lifestring("XX\nX ") == set([(0,0), (0,1), (1,0)])


# ____________________________________________________________
# Aufgabe 3

def test_make_coding():
    freq = {"a": 1, "b": 2, "c": 5, "d": 18}
    tree = make_tree(freq)
    assert tree.right.value == "d"
    assert tree.left.right.value == "c"
    assert tree.left.left.right.value == "b"
    assert tree.left.left.left.value == "a"

def test_mapping():
    freq = {"a": 1, "b": 2, "c": 5, "d": 18}
    tree = make_tree(freq)
    mapping = make_mapping(tree)
    assert mapping["a"] == "000"
    assert mapping["b"] == "001"
    assert mapping["c"] == "01"
    assert mapping["d"] == "1"

def test_encode():
    freq = {"a": 1, "b": 2, "c": 5, "d": 18}
    tree = make_tree(freq)
    mapping = make_mapping(tree)
    s = encode(mapping, "ddaccddb")
    assert s == "11000010111001"

def test_encode():
    freq = {"a": 1, "b": 2, "c": 5, "d": 18}
    tree = make_tree(freq)
    s = decode(tree, "1010001010110100101000101")
    assert s == "dcadccdcbcadc"
