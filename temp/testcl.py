def my_sum(ma, mb):
    return ma + mb


class my_class(object):
    a = 1
    b = 2

    # def __init__(self, aa, bb):
    #     a = aa
    #     b = bb


cl = my_class()
print("a ", cl.a)
print("b ", cl.b)
print("my_sum ", my_sum(10, 20))


class SomeClass(object):
    def method1(self, x):
        return 2 * x


obj = SomeClass()
print(obj.method1(7))


class Point(object):
    def __init__(self, x, y, z):
        self.coord = (x, y, z)


p = Point(13, 14, 15)
print("coord ", p.coord[0])  # (13, 14, 15)


class SomeClass(object):
    pass


def squaremethod(self, x):
    return x * x


SomeClass.square = squaremethod
obj = SomeClass()
print("square ", obj.square(5))  # 25


class SomeClass(object):
    def __new__(cls):
        print("new")
        return super(SomeClass, cls).__new__(cls)

    def __init__(self):
        print("init")

obj = SomeClass();


