from random_generator import Random_Generator as rnd

class Animal:
    def __init__(self, animalNo = "", gender = "", birthDate = "", colour = "", weight = 0, conditions=""):
        if (len(animalNo) > 1):
            self.animalNo = animalNo
        else:
            self.animalNo = rnd.random_generator(self,4)
        self.gender = gender
        self.birthDate = birthDate
        self.colour = colour
        self.weight = weight
        self.conditions = conditions

        