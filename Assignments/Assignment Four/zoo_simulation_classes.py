# Zoo simulation classes
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Lion(Animal):
    def roar(self):
        return "Roar!"

class Elephant(Animal):
    def trumpet(self):
        return "Trumpet!"

lion = Lion("Leo", "Lion")
elephant = Elephant("Ellie", "Elephant")
print(lion.roar())
print(elephant.trumpet())
