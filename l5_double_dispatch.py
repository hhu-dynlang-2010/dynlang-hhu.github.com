class Int(object):
    def __init__(self, val):
        self.val = val

    def add(self, other):
        return other.add_int(self)

    def add_int(self, other):
        return int.__add__(self.val, other.val)

    def add_float(self, other):
        return float.__add__(float(self.val), other.val)

class Float(object):
    def __init__(self, val):
        self.val = float(val)

    def add(self, other):
        return other.add_float(self)

    def add_float(self, other):
        return float.__add__(self.val, other.val)

    def add_int(self, other):
        return float.__add__(self.val, float(other.val))
