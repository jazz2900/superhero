dogs = list()
dogs.append("German Shepherd")
dogs.append("Poodle")
print(dogs)

class Dog:
    def bark(self):
        print("Woof!")


class Dog:
    greeting = "Woof!"

    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.greeting)


if __name__ == "__main__":
    my_dog = Dog()
    my_dog.bark()
