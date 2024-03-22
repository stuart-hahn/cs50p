import random


class Hat:
    houses = ["Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"]

    @classmethod
    def sort(cls, name):
        house = random.choice(cls.houses)
        print(name, "is in", house)


Hat.sort("Harry")
Hat.sort("Hermione")
Hat.sort("Ron")
