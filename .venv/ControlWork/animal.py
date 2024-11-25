class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an animal"

class Cat(Animal):
    def speak(self):
        return "Meow"

class Dog(Animal):
    def speak(self):
        return "Woof"

dog = Dog('Buddy')
cat = Cat("Kitty")

print(dog.name, dog.speak())
print(cat.name, cat.speak())