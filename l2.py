def test_remove_duplicates():
    l = remove_duplicates([])
    assert l == []
    l = remove_duplicates([1, 1, 1, 2, 3, 4, 5, 4, 6])
    assert l == [1, 2, 3, 4, 5, 6]

def remove_duplicates(l):
    result = []
    seen = {}
    for element in l:
        if element not in seen:
            result.append(element)
            seen[element] = True
    return result

def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(9) == 34
    assert fib(35) == 9227465

def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

results = {}
def fib_memoized(n):
    if n in results:
        return results[n]
    if n == 1 or n == 2:
        return 1
    result = fib(n - 1) + fib(n - 2)
    results[n] = result
    return result

def memo_maker(f):
    results = {}
    def memoized(*args):
        if args in results:
            return results[args]
        result = f(*args)
        results[args] = result
        return result
    return memoized

def test_memo_maker():
    l = []
    def change_list(n):
        l.append(n)
        return len(l)
    memoized = memo_maker(change_list)
    r = memoized(1)
    assert r == 1
    assert l == [1]
    r = memoized(1)
    assert r == 1
    assert l == [1]

def make_adder(n):
    def add(x):
        return x + n
    return add

def test_make_adder():
    add5 = make_adder(5)
    assert add5(10) == 15
