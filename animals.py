class Tiger:
    """A tiger has a name and age and favorite food."""

    # when we use the = argument it makes that var optional
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
        self.favorite_food = "catnip"

    def __str__(self):
        return "{} is {} years old".format(self.name, self.age)

    def eat(self, food):
        return "{} eats {}".format(self.name, food)


tony = Tiger("Tiger", 66)
#print(tony.name + " is " + str(tony.age) + "years old")
print("{} is {} years old".format(tony.name, tony.age))
print(tony)
tony.favorite_food = 'Frosted Flakes™'
print("{}'s favorite food is {}".format(tony.name, tony.favorite_food))
tony.eat(tony.favorite_food)

hobbes = Tiger("Hobbes")
print(hobbes)
hobbes.age = 24
print(hobbes)
hobbes.eat("fish")
print(hobbes)
