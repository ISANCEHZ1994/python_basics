class Pets():
    animals = []

    def __init__(self, animals):
        self.animals = animals
    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Steve(Cat):
    def sing(self, sounds):
        return f'{sounds}'

simon = Simon("Simon", 1)
sally = Sally("Sally", 2)
steve = Steve("Steve", 3)

my_cats = [simon, sally, steve]
all_pets = Pets(my_cats)

print()
all_pets.walk()
print()
