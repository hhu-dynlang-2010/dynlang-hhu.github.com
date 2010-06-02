class IFile(object):
    def __init__(self):
        raise NotImplementedError("interface")
    def m(self):
        raise NotImplementedError("interface")
    def read(self):
        raise NotImplementedError("abstract base")
    def readall(self):
        res = []
        while True:
            s = self.read()
            res.append(s)
            if not s:
                break
        return "".join(res)
        

class ReaderBase(object):
    def m(self):
        pass

class StdInReader(ReaderBase, IFile):
    def __init__(self):
        pass
    def read(self):
        import os
        return os.read(0, 1024)

def print_from_file(f):
    print f.readall()
