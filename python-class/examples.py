
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
    def get_age(self):
        return self.age

p1 = person('Bob', 12)
print(p1)
print(p1.name, p1.age)