class Person:
    def __init__(self, name, age, city) -> None:
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        return f'Привет, меня зовут {self.name}, мне {self.age} лет, я проживаю в {self.city}'

people = Person('Искендер', 22, "Оше")
print(people.introduce())