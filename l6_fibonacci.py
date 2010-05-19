
def test_fib_iter():
    count = 0
    l = [1, 1, 2, 3, 5, 8, 13]
    for f in Fib():
        assert f == l[count]
        count += 1
        if count >= len(l):
            break

class Fib(object):
    def __init__(self):
        self.a = 1
        self.b = 1
    
    def __iter__(self):
        return self

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        return self.b - self.a

def generate_fib():
    a = 1
    b = 1
    while True:
        yield a
        a, b = b, a + b


def primes():
    import math
    known_primes = [2]
    yield 2
    candidate = 3
    while True:
        prime = True
        sqrtcand = math.sqrt(candidate)
        for x in known_primes:
            if candidate % x == 0:
                prime = False
                break
            if x > sqrtcand:
                break
        if prime:
            known_primes.append(candidate)
            yield candidate
        candidate += 2

def first_five_primes():
    p = primes()
    print p.next()
    print p.next()
    print p.next()
    print p.next()
    print p.next()

def filter_odd(gen):
    for x in gen:
        if x % 2 == 0:
            yield x

def passthrough_yield12(gen):
    yield 1
    yield 2
    for value in gen:
        yield value

def enumerate(gen):
    i = 0
    for elt in gen:
        yield i, elt
        i += 1


