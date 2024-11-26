# Base class: Animal
class Animal:
    def move(self):
        print("The animal is moving.")

# Subclass of Animal: Snake
class Snake(Animal):
    def move(self):
        print("The snake is slithering on the ground 🐍")

# Subclass of Animal: Kangaroo
class Kangaroo(Animal):
    def move(self):
        print("The kangaroo is hopping across the ground 🦘")

# Subclass of Animal: Shark
class Shark(Animal):
    def move(self):
        print("The shark is swimming in the water 🦈")

# Subclass of Animal: Cheetah
class Cheetah(Animal):
    def move(self):
        print("The cheetah is running at high speed 🐆")

# Create instances of each class
animals = [Snake(), Kangaroo(), Shark(), Cheetah()]

# Polymorphism of animals
print("Animal moves:")
for animal in animals:
    animal.move()  # Different ways animals move
