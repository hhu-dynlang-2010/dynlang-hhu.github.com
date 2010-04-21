# _________________________________________________________
# remove duplicates

def test_remove_duplicates():
    assert remove_duplicates([1, 1, 2, 4, 6, 1, 5]) == [1, 2, 4, 6, 5]
    assert remove_duplicates([]) == []


def remove_duplicates(l):
    result = []
    d = {}
    for element in l:
        if element not in d:
            result.append(element)
            d[element] = True
    return result

# _________________________________________________________
# naively recursive fibonacci

def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(9) == 34
    assert fib(35) == 9227465

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        result = fib(n - 1) + fib(n - 2)
        return result

# _________________________________________________________
# memoized recursive fibonacci

def test_fib_memo():
    assert fib_memo(1) == 1
    assert fib_memo(2) == 1
    assert fib_memo(3) == 2
    assert fib_memo(9) == 34
    assert fib_memo(35) == 9227465

d_fib = {}
def fib_memo(n):
    if n in d_fib:
        return d_fib[n]
    if n == 1 or n == 2:
        return 1
    else:
        result = fib_memo(n - 1) + fib_memo(n - 2)
        d_fib[n] = result
        return result

# _________________________________________________________
# simple example for an inner function

def make_adder(n):
    def addn(x):
        return x + n
    return addn

def test_make_adder():
    add5 = make_adder(5)
    assert add5(5) == 10
    assert add5(7) == 12


# _________________________________________________________
# generate memoizing function automatically

def memo_maker(f):
    d = {}
    def memoized(n):
        if n in d:
            return d[n]
        result = f(n)
        d[n] = result
        return result
    return memoized

def test_memo_maker():
    l = []
    def change_list(n):
        l.append(n)
        return len(l)
    change_list_memo = memo_maker(change_list)
    r = change_list_memo(0)
    assert r == 1

    r = change_list_memo(0)
    assert r == 1


def fib_memo_generated(n):
    if n == 1 or n == 2:
        return 1
    else:
        result = fib_memo_generated(n - 1) + fib_memo_generated(n - 2)
        return result
fib_memo_generated = memo_maker(fib_memo_generated)

def test_fib_memo_generated():
    assert fib_memo_generated(1) == 1
    assert fib_memo_generated(2) == 1
    assert fib_memo_generated(3) == 2
    assert fib_memo_generated(9) == 34
    assert fib_memo_generated(35) == 9227465
