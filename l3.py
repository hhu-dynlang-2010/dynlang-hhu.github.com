class NoMatch(Exception):
    pass

class State1(object):
    def transition(self, c):
        if c == "a":
            self.__class__ = State2
        else:
            raise NoMatch

    def is_final(self):
        return True


class State2(object):
    def transition(self, c):
        if c == "b":
            self.__class__ = State1
        else:
            raise NoMatch

    def is_final(self):
        return False

def match(s):
    machine = State1()
    for c in s:
        try:
            machine.transition(c)
        except NoMatch:
            return False
    return machine.is_final()

def test_match():
    assert match("ababab") == True
    assert match("abababababab") == True
    assert match("aba") == False
    assert match("abac") == False


