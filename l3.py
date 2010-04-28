class State0(object):
    final = True
    def transition(self, c):
        if c == "a":
            self.__class__ = State1
            return True
        return False

class State1(object):
    final = False
    def transition(self, c):
        if c == "b":
            self.__class__ = State0
            return True
        return False

def match(s):
    state = State0()
    for c in s:
        if not state.transition(c):
            return False
    return state.final 


def test_match():
    assert match("")
    assert match("ababab")
    assert not match("abc")
    assert not match("aba")

