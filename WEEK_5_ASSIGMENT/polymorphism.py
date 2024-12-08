class Animal:
  """Base class for animals."""

  def move(self):
    """Generic move method."""
    raise NotImplementedError("Subclasses must implement move()")

class Dog(Animal):
  def move(self):
    print("Running")

class Bird(Animal):
  def move(self):
    print("Flying")

class Fish(Animal):
  def move(self):
    print("Swimming")

# Example usage:
my_dog = Dog()
my_bird = Bird()
my_fish = Fish()

my_dog.move()  # Output: Running
my_bird.move()  # Output: Flying
my_fish.move()  # Output: Swimming