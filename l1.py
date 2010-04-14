import py


def dot_product(v1, v2):
    assert len(v1) == len(v2)
    sum = 0
    for i in range(len(v1)):
        prod = v1[i] * v2[i]
        if sum == 0:
            sum = prod
        else:
            sum = sum + prod
    return sum

def test_dot_product():
    assert dot_product([10, 10, 10], [2, 3, 4]) == 90
    assert dot_product([], []) == 0
    py.test.raises(AssertionError, dot_product, [], [5])

def test_abusing_dot_product():
    assert dot_product([2, 3, 4], ["ab", "cd", "ef"]) == "ababcdcdcdefefefef"


def divisors(n):
    result = []
    for i in range(1, n+1):
        if n % i == 0:
            result.append(i)
    return result

def is_prime(n):
    div = divisors(n)
    return len(div) == 2

def test_is_prime():
    assert is_prime(5) == True
    assert is_prime(4) == False
    assert is_prime(11) == True
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(9) == False

def test_divisors():
    assert divisors(5) == [1, 5]
    assert divisors(4) == [1, 2, 4]
