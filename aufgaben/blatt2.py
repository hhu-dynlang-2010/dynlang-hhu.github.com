import py


# ____________________________________________________________
#
# AUFGABE 1
#
def test_word_occurences():
    d = compute_word_occurences("a b a b a c a c")
    assert d == {
        "a": {"b": 2, "c": 2},
        "b": {"a": 2},
        "c": {"a": 1}
    }

def test_word_occurences_long():
    f = open("faust_1")
    s = f.read()
    f.close()
    d = compute_word_occurences(s)
    assert d["FAUST:"]["Habe"] == 1
    assert d["Habe"]["nun,"] == 1
    assert d["nun,"]["ach!"] == 1
    assert d["GRETCHEN:"] == {
        'Wieso?': 1,
        'Kein': 1,
        'Nachbarin!': 1,
        'Mein': 2,
        'Meine': 1,
        'Weh!': 1,
        'Allm\xe4chtiger!': 1,
        'W\xe4r': 1,
        '(nach': 1,
        'Das': 2,
        'Mir': 1,
        'Ach!': 1,
        'Er': 1}

def test_random_words():
    f = open("faust_1")
    s = f.read()
    f.close()
    d1 = compute_word_occurences(s)
    text = make_random_text(d1, 100)
    d2 = compute_word_occurences(text)
    last = None
    for word in text.split():
        if last is not None:
            assert word in d1[last]
        last = word
    print text


# ____________________________________________________________
#
# AUFGABE 2
#
def test_mygetattr_override():
    class A(object):
        pass
    register_override(object, "fortytwo", 42)
    register_override(A, "fortyone", 41)
    a = A()
    assert mygetattr(a, "fortytwo") == 42
    assert mygetattr(a, "fortyone") == 41
    assert mygetattr([], "fortytwo") == 42
    py.test.raises(AttributeError, mygetattr, 1, "fortyone")


# ____________________________________________________________
#
# AUFGABE 4
#


def burrows_wheeler_forward(s):
    strings = []
    for i in range(len(s)):
        strings.append(s[i:] + s[:i])
    strings.sort()
    i = strings.index(s)
    output = ''.join([s[-1] for s in strings])
    return (output, i)


def test_forward_transformation():
    # see http://de.wikipedia.org/wiki/Burrows-Wheeler-Transformation
    assert burrows_wheeler_forward("TEXTUEL") == ("UTELXTE", 3)

    input = ("TRENTATRE.TRENTINI.ANDARONO.A.TRENTO"
             ".TUTTI.E.TRENTATRE.TROTTERELLANDO")
    expected_output = ("OIIEEAEO..LDTTNN.RRRRRRRTNTTLE"
                       "AAIOEEEENTRDRTTETTTTATNNTTNNAAO....OU.T")
    assert burrows_wheeler_forward(input) == (expected_output, 60)
