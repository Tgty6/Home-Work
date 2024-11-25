class Person:
    def __init__(self):
        self._age = 0

    def set_age(self, age):
        if age < 0:
            raise ValueError("Ошибка")
        self._age = age

    def get_age(self):
        return self._age

try:
    p = Person()
    p.set_age(25)
    print(p.get_age())

    p.set_age(-5)
except ValueError as e:
    print(e)
