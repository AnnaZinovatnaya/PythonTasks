def singleton(cls):
    was = {}
    def wrapper(*args):
        key = (cls, args)
        if key not in was:
            was[key] = cls(args)
        return was[key]
    return wrapper


@singleton
class A:
    def __init__(self, a):
        self.a = a


a1 = A(5)
print(id(a1))
a2 = A(5)
print(id(a2))

a3 = A(6)
print(id(a3))
a4 = A(6)
print(id(a4))
