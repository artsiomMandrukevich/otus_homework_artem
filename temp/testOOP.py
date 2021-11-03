class SomeClass():
    attr1 = 42

    def __getattr__(self, attr):
        return attr.upper()


obj = SomeClass()
print("obj.attr1", obj.attr1)
print("obj.attr2", obj.attr2)
